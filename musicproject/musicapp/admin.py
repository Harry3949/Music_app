from django.contrib import admin
from .models import Category, MusicPost,Comment

class CategoryAdmin(admin.ModelAdmin):
    #レコード一覧にidとtitleを表示
    list_display = ('id','title')
    #表示するカラムにリンク設定
    list_display_links = ('id','title')
    
class MusicPostAdmin(admin.ModelAdmin):
    #レコード一覧にidとtitleを表示
    list_display = ('id','title')
    #表示するカラムにリンクを設定
    list_display_links = ('id','title')

class CommentAdmin(admin.ModelAdmin):
    # 管理画面で表示する項目を指定
    list_display = ('comments', 'user', 'posted_at')
    # フィルタリング機能を追加（ユーザー、投稿、投稿日時でフィルタリング）
    list_filter = ('user', 'posted_at')
 

    


#Django管理サイトにCategory,CategoryAdminを登録
admin.site.register(Category, CategoryAdmin)
#Django管理サイトにPhotoPost、PhotoPostAdminを登録
admin.site.register(MusicPost)
admin.site.register(Comment,CommentAdmin)
    