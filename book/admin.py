from django.contrib import admin
from book.models import Publisher, Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email']
	search_fields = ['first_name', 'last_name']

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)