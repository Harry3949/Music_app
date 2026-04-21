from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリー',
        max_length=20)
    
    def __str__(self):
        return self.title


class MusicPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200,
    )
    content = models.TextField(
        verbose_name = '本文',
    )
    image = models.ImageField(
        verbose_name='画像ファイル',
        upload_to='images/',  # 画像ファイルが保存されるディレクトリ
    )
    music_file = models.FileField(
        verbose_name='音楽ファイル',
        upload_to='music_files/',
    )
    posted_at = models.DateTimeField(
        verbose_name= '投稿日時',
        auto_now_add= True,
    )
    likes = models.ManyToManyField(
        CustomUser,
        verbose_name='いいね',
        related_name='liked_music',
        blank=True
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    comments = models.TextField(
        verbose_name='コメント',
        )
    posted_at =models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )