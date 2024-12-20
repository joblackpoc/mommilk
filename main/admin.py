from django.contrib import admin
from .models import Post, Profile, Categories, Infomation, Team, About
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','post_title','published_date']
    list_display_links = ['id','post_title']
    list_filter = ['published_date']
    search_fields = ['post_title']


admin.site.register(Profile)
admin.site.register(Categories)
admin.site.register(Infomation)
admin.site.register(Team)
admin.site.register(About)