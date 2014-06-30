from django import forms
from models import UserGoogleQuery, GoogleQuery, GoogleSuggestion
from util import download_suggestions

class GoogleQueryForm(forms.ModelForm):
    google_query = forms.CharField(max_length=50)
    class Meta:
        model = UserGoogleQuery
        exclude = ['suggestions', 'inspiration_query', 'inspiration_item', 'user', 'meaning_comment', 'humorous_comment']

    def __init__(self, *args, **kwargs):
        super(GoogleQueryForm, self).__init__(*args, **kwargs)
        self.original_query_terms = ''

    def clean_google_query(self):
        """Hack so that cleaning charfield on form returns object to relate to"""
        data = self.cleaned_data['google_query']
        self.original_query_terms = data
        query_data = ' '.join(data.split())
        self.obj, created = GoogleQuery.objects.get_or_create(query_terms=query_data)
        return self.obj

    def process_suggestions(self):
        return self.save_suggestions(self.get_suggestions())

    def get_suggestions(self):
        suggestions_list = download_suggestions(self.original_query_terms)
        return suggestions_list

    def save_suggestions(self, suggestions_list):
        return [GoogleSuggestion.objects.get_or_create(search_text=sug_text[0])[0] for sug_text in suggestions_list]

