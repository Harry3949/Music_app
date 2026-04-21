from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import MusicPost, Comment
from .forms import MusicPostForm, CommentForm, ContactForm

def photo_edit(request, pk):
    """音楽投稿の編集ビュー"""
    post = get_object_or_404(MusicPost, pk=pk)
    
    if request.method == 'POST':
        form = MusicPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('musicapp:photo_detail', pk=post.pk)
    else:
        form = MusicPostForm(instance=post)
    
    return render(request, 'photo_edit.html', {'form': form, 'post': post})



def index_view(request):
    """トップページ（一覧表示と検索）ビュー"""
    query = request.GET.get('search')
    if query:
        records = MusicPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).order_by('-posted_at')
    else:
        records = MusicPost.objects.all().order_by('-posted_at')
    
    # 全コメントを取得（最新順）
    comments = Comment.objects.all().order_by('-posted_at')
    
    paginator = Paginator(records, 9)
    page_number = request.GET.get('page', 1)
    pages = paginator.page(page_number)
   
    return render(request, 'index.html', {
        'page_obj': pages,
        'comments': comments
    })

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('musicapp:contact')
    def form_valid(self, form):
        name=form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        from_email = 'admin@example.com'
        to_list = ['admin@example.com']
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました、')
        return super().form_valid(form)
    
    
@method_decorator(login_required, name="dispatch")
class CreateMusicView(CreateView):
    form_class=MusicPostForm
    template_name = "post_photo.html"
    success_url = reverse_lazy('musicapp:post_done')
    
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    #index.htmlをレンダリング
    template_name='index.html'
    #1ページに表示するレコードの件数
    paginate_by = 9
    
    def get_queryset(self):
        #self.kwargsでキーワードの辞書を取得し、Categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category']
        #filterで絞り込む
        categories = MusicPost.objects.filter(
            category=category_id).order_by('-posted_at')
        #クエリによって取得されたレコード返す
        return categories

class UserView(ListView):
    #index.htmlをレンダリング
    template_name='index.html'
    #1ページに表示するレコードの件数
    paginate_by = 9
    
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = MusicPost.objects.filter(
            user=user_id).order_by('-posted_at')
        #クエリによって取得されたレコード返す
        return user_list

class MypageView(ListView):
    """マイページ（ログインユーザーの投稿一覧）ビュー"""
    template_name = 'mypage.html'
    paginate_by = 9
    
    def get_queryset(self):
        #filter(userフィールド=userオブジェクトで絞り込み)
        queryset = MusicPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset
    
class DetailView(DetailView):
    #post.htmlをレンダリングする
    template_name = 'detail.html'
    #クラス変数modelにモデルBlogPostを設定
    model = MusicPost

class PhotoDeleteView(DeleteView):
    model = MusicPost
    template_name = 'delete.html'
    success_url = reverse_lazy('musicapp:mypage')  # 名前空間を修正

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class CreateCommentView(CreateView):
   
    form_class = CommentForm
   
    template_name = 'comment_post.html'
   
    success_url = reverse_lazy('musicapp:post_done')
   
    def form_valid(self, form):
       
        commentdata = form.save(commit=False)
       
        commentdata.user = self.request.user
       
        commentdata.save()
       
       
        return super().form_valid(form)
    
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    return redirect('musicapp:index')
 
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('musicapp:index')  # 適切なリダイレクト先を設定
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

@login_required
def like_music_view(request, pk):
    """音楽投稿に対するいいねの切り替えView"""
    post = get_object_or_404(MusicPost, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    # AJAX(Fetch)リクエストの場合はJSONを返す
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'total_likes': post.total_likes()
        })
    
    # 通常のリクエストは詳細ページへリダイレクト
    return redirect('musicapp:photo_detail', pk=pk)