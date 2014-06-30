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
    (r'^accounts/profile/', ProfileView.as_view()),
)

# core views
urlpatterns += patterns('core.views',
    # Examples:
    # url(r'^$', 'revealing_questions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', HomePageView.as_view(), {}, 'home'),
    (r'^home/$', HomePageView.as_view(), {}, 'home'),
    (r'^searchquery/create/$', CreateQueryView.as_view(), {}, 'create_query'),
    (r'^searchquery/view/(?P<pk>\d+)/$', ViewQueryView.as_view(), {}, 'view_query'),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )