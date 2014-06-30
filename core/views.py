from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import UserGoogleQuery, UserQuerySuggestion


# a query view to see one query , its results, and its comments etc

# a user view to see a user's queries and comments and activity

# list pages to see queries by tags and by categories and by users

#
# a main home page view to see categories and popular queries

from forms import GoogleQueryForm
from django.views.generic.edit import CreateView, View
from django.views.generic.detail import DetailView

class HomePageView(View):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})


class ProfileView(HomePageView):
    pass


class CreateQueryView(CreateView):
    template_name = 'create_query.html'
    # model = UserGoogleQuery #TODO- is this needed at all?
    form_class = GoogleQueryForm

    def form_valid(self, form):
        http_response =  super(CreateQueryView, self).form_valid(form)
        suggestions_list = form.process_suggestions()
        for index, result in enumerate(suggestions_list):
            UserQuerySuggestion.objects.create(suggestion=result, user_query=self.object, rank=index+1)
        return http_response

    def get_success_url(self):
        return reverse('view_query', kwargs={'pk':str(self.get_form(self.form_class).instance.id)})


class ViewQueryView(DetailView):
    model = UserGoogleQuery
    template_name = 'view_query.html'
