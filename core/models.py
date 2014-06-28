from django.db import models
from django.contrib.auth.models import User

class GoogleQuery(models.Model):
	query_terms = models.TextField()
	# created_on = models.DateTimeField(auto_now_add=True)
	# submitted = models.BooleanField()
	# submitted_on = models.DateTimeField(null=True)

	def __unicode__(self):
		return self.query_terms
		
class GoogleSuggestion(models.Model):
	suggestions = models.TextField()
	# created_on = models.DateTimeField(auto_now_add=True)

class UserGoogleQuery(models.Model):
	google_query = models.ForeignKey('GoogleQuery', related_name='google_query_set')
	suggestions = models.ManyToManyField('GoogleSuggestion', through='UserQuerySuggestion')
	user = models.ForeignKey('auth.User')
	created_on = models.DateTimeField(auto_now_add=True)
	inspiration_query = models.ForeignKey('GoogleQuery', null=True, default=None, related_name='inspiration_query_set')
	inspiration_item = models.ForeignKey('UserGoogleQuery', null=True, default=None)
	meaning_comment = models.TextField(blank=True)
	humurous_comment = models.TextField(blank=True)

	def __unicode__(self):
		return '{} - created by {}'.format(self.google_query.query_terms, self.user.username)

class UserQuerySuggestion(models.Model):
	user_query = models.ForeignKey('UserGoogleQuery')
	suggestion = models.ForeignKey('GoogleSuggestion')
	rank = models.PositiveIntegerField()

# Because everything has a meaning:
 
# Because nothing is that serious: 

# admin user
# malka_admin , admin2134malka

# comments

# categories: list made by me: humor, graphic, lgbt, science, celebrities, puns, sarcasm, duh, biology, men, women, politics, 
#  controversy, compare, contrast, 
# tags - users choose and create

# url's: by user, tag, category, 
# sorty by: date, popularity, notoriety

# compare and contrast two together: submit that way to begin with


# repeat attempts: option to add a compare/contrast, or option to leave a comment

# similar too... link them indefinitely !!! maximize views by linking to already existing queries
# similarity types: inspired from, as _adjective_ as, (this way people see what others with similar tastes liked)

# should we show a little box of queries whose text is very similar: 'why do men h' and 'why do men have' and 'do men have'




