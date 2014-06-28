from django.contrib import admin

from models import *

admin.site.register(GoogleQuery)
admin.site.register(GoogleSuggestion)
admin.site.register(UserQuerySuggestion)
admin.site.register(UserGoogleQuery)

