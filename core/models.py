from django.db import models
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags

class BaseFields(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

class GoogleQuery(BaseFields):
    """The search terms that a user might start typing in to a google search box"""
    query_terms = models.TextField()

    def __unicode__(self):
        return self.query_terms

    @property
    def latest_suggestion_set(self):
        return self.latest_userquery.suggestions.all()

    @property
    def latest_userquery(self):
        return self.google_query_set.latest('created_on')

    @property
    def get_latest_userquery_url(self):
        return reverse('view_query', kwargs={'pk':str(self.latest_userquery.id)})

class GoogleSuggestion(BaseFields):
    """A search suggestion from google's auto-suggest dropwdown"""
    search_text = models.TextField()

    def __unicode__(self):
        return self.search_text

    @property
    def google_search_url(self):
        return 'https://www.google.com/?#q={}'.format('+'.join(strip_tags(self.search_text).split()))

class UserGoogleQuery(BaseFields):
    """
    A user's attempt at entering a search and the suggestions that google responds with
    with addditional fields to allow the user to react and comment on the response
    """
    google_query = models.ForeignKey('GoogleQuery', related_name='google_query_set')
    suggestions = models.ManyToManyField('GoogleSuggestion', through='UserQuerySuggestion')
    user = models.ForeignKey('auth.User')
    inspiration_query = models.ForeignKey('GoogleQuery', null=True, default=None, related_name='inspiration_query_set')
    inspiration_item = models.ForeignKey('UserGoogleQuery', null=True, default=None)
    meaning_comment = models.TextField(blank=True)
    humorous_comment = models.TextField(blank=True)

    def __unicode__(self):
        return '{} - created by {}'.format(self.google_query.query_terms, self.user.username)

    def get_absolute_url(self):
        return reverse('view_query', kwargs={'pk':str(self.id)})

class UserQuerySuggestion(models.Model):
    """A many-to-many table to rank the suggestions like google does"""
    user_query = models.ForeignKey('UserGoogleQuery')
    suggestion = models.ForeignKey('GoogleSuggestion')
    rank = models.PositiveIntegerField()

    def __unicode__(self):
        return 'userquery id {} suggestion rank {}'.format(self.user_query.id, self.rank)
