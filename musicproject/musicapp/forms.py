from django.forms import ModelForm
from django import forms
from .models import MusicPost
from .models import Comment

class MusicPostForm(ModelForm):
    class Meta:
        model = MusicPost
        fields = ['title', 'content', 'image', 'music_file',]
        
class ContactForm(forms.Form):
    name = forms.CharField(label='ユーザー名')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
            'ユーザー名を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder']= \
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder']= \
            'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder']= \
            'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'      
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']