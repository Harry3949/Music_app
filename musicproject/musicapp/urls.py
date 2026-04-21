from django.urls import path
from .import views

app_name = 'musicapp'

urlpatterns = [
    path('',views.index_view,name='index'),
    path('post/',views.CreateMusicView.as_view(), name=('post')),
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    path('photos/<int:category>',views.CategoryView.as_view(),name = 'photos_cat'),
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    path('photo-detail/<int:pk>',views.DetailView.as_view(),name = 'photo_detail'),
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    path('comment/',views.CreateCommentView.as_view(),name='comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('like-music/<int:pk>/', views.like_music_view, name='like_music'),
]
