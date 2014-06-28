from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'revealing_questions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# allauth views
urlpatterns += patterns('',
    (r'^accounts/', include('allauth.urls')),
)

# core views
urlpatterns += patterns('core.views',
    # Examples:
    # url(r'^$', 'revealing_questions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^home/$', HomePageView.as_view(), {}, 'home'),
    (r'^google/create/$', CreateQueryView.as_view(), {}, 'create_query'),
    (r'^google/create/thanks/$', ViewQueryView.as_view(), {}, 'created_thanks'),
)