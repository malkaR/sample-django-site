from django.shortcuts import render
# from django.http import HttpResponse

# a view to create a google query

# a query view to see one query , its results, and its comments etc

# a user view to see a user's queries and comments and activity

# list pages to see queries by tags and by categories and by users

#
# a main home page view to see categories and popular queries

# views.py
from forms import GoogleQueryForm
from django.views.generic.edit import FormView, CreateView, View

class HomePageView(View):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

class ProfileView(HomePageView):
    pass

class CreateQueryView(CreateView):
    template_name = 'create_query.html'
    form_class = GoogleQueryForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.


        http_response =  super(CreateQueryView, self).form_valid(form)
        form.get_suggestions()
        return http_response

    def get_success_url(self):
    	return '/google/create/thanks/'

class ViewQueryView(View):
	template_name = 'thanks.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'content': 'you are awesome'})








# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.views.generic import View

# from .forms import MyForm

# class MyFormView(View):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/success/')

#         return render(request, self.template_name, {'form': form})
