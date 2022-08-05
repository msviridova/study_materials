from django.contrib import admin
from .models import Books, Author, Tag


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title', 'author')
    list_filter = ('tags',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_display_links = ('tag',)
    search_fields = ('tag',)


admin.site.register(Books, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)

