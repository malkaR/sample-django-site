# django
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# external apps
from allauth.account.decorators import login_required

# Internal apps
from models import UserGoogleQuery, UserQuerySuggestion
from forms import GoogleQueryForm, GoogleQuery



# a query view to see one query , its results, and its comments etc

# a user view to see a user's queries and comments and activity

# list pages to see queries by tags and by categories and by users

#
# a main home page view to see categories and popular queries


class LoginRequiredBaseView(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredBaseView, self).dispatch(*args, **kwargs)

class HomePageView(ListView):
    model = GoogleQuery
    template_name = 'home.html'

# 	def get(self, request, *args, **kwargs):
# 		return render(request, self.template_name, {})


class ProfileView(HomePageView):
    pass


class CreateQueryView(LoginRequiredBaseView, CreateView):
    template_name = 'create_query.html'
    # model = UserGoogleQuery #TODO- is this needed at all?
    form_class = GoogleQueryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        # first validate and save form so that cleaning creates the googlequery object
        http_response =  super(CreateQueryView, self).form_valid(form)
        # now get and save suggestions
        suggestions_list = form.process_suggestions()
        for index, result in enumerate(suggestions_list):
            UserQuerySuggestion.objects.create(suggestion=result, user_query=self.object, rank=index+1)
        return http_response

    def get_success_url(self):
        return reverse('view_query', kwargs={'pk':str(self.get_form(self.form_class).instance.id)})


class ViewQueryView(LoginRequiredBaseView, DetailView):
    model = UserGoogleQuery
    template_name = 'view_query.html'
