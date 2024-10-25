from django.contrib import admin
from .models import Post, Author, Category, Tag, Image, Comment, Quote, Skill


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'author')
    search_fields = ('name', 'description')
    list_filter = ('categories', 'tags', 'date')
    filter_horizontal = ('categories', 'tags')
    readonly_fields = ('date',)
    prepopulated_fields = {'name': ('description',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'flag_about')
    search_fields = ('first_name', 'last_name', 'bio')
    list_filter = ('flag_about',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')
    search_fields = ('post__name',)  # Поиск по названию поста

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'public_date')
    search_fields = ('name', 'email', 'comment')
    list_filter = ('public_date',)

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('number', 'quote', 'author')
    search_fields = ('quote', 'author__first_name', 'author__last_name')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'author')
    search_fields = ('skill', 'author__first_name', 'author__last_name')

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Skill, SkillAdmin)
