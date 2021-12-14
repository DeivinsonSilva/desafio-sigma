from django.contrib import admin

from sigma.models import Quote

class Quotes(admin.ModelAdmin):
    list_display = ('id', 'author', 'author_quote')
    list_display_links = ('id', 'author')
    search_fields = ('author',)

admin.site.register(Quote, Quotes)