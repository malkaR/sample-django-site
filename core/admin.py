from django.contrib import admin

from models import *

class UserQuerySuggestionInline(admin.StackedInline):
    model = UserQuerySuggestion
    extra = 0
    max_num = 4

class UserGoogleQueryAdmin(admin.ModelAdmin):
    #list_display = ('user__username', 'last_name')
    list_filter = ('user__username', 'created_on')
    search_fields = ['google_query__query_terms', 'suggestions__userquerysuggestion__suggestion__suggestions']
    inlines = [UserQuerySuggestionInline]

admin.site.register(GoogleQuery)
admin.site.register(GoogleSuggestion)
admin.site.register(UserQuerySuggestion)
admin.site.register(UserGoogleQuery, UserGoogleQueryAdmin)

