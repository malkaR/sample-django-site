from django import forms
import models as models
from util import download_suggestions

class GoogleQueryForm(forms.ModelForm):
	google_query = forms.CharField(max_length=50)
	class Meta:
		model = models.UserGoogleQuery
		exclude = ['suggestions', 'inspiration_query', 'inspiration_item']

	def __init__(self, *args, **kwargs):
		super(GoogleQueryForm, self).__init__(*args, **kwargs)
		self.original_query_terms = ''

	def clean_google_query(self):
		"""Hack so that cleaning charfield on form returns object to relate to"""
		data = self.cleaned_data['google_query']
		self.original_query_terms = data
		query_data = ' '.join(data.split())
		obj, created = models.GoogleQuery.objects.get_or_create(query_terms=query_data)
	 	return obj
	
	def save(self, *args, **kwargs):
		
		
		super(GoogleQueryForm, self).save(*args, **kwargs)

	def get_suggestions(self):
		
		download_suggestions(self.original_query_terms)

	# def save(self, *args, **kwargs):
		