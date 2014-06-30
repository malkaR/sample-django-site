from django.contrib import admin
import models

class UserQuerySuggestionInline(admin.StackedInline):
    model = models.UserQuerySuggestion
    extra = 0
    max_num = 4

class UserGoogleQueryAdmin(admin.ModelAdmin):
    list_filter = ('user__username', 'created_on')
    search_fields = ['google_query__query_terms', 'suggestions__userquerysuggestion__suggestion__suggestions']
    inlines = [UserQuerySuggestionInline]

admin.site.register(models.GoogleQuery)
admin.site.register(models.GoogleSuggestion)
admin.site.register(models.UserQuerySuggestion)
admin.site.register(models.UserGoogleQuery, UserGoogleQueryAdmin)

