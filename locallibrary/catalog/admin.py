from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

admin.site.register(Genre)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'display_photo')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death', 'photo')]

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.photo.url))
        return "No Image"

    display_photo.short_description = 'Photo'

admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )