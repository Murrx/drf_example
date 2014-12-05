from django.conf.urls import patterns, include, url
from django.contrib import admin
from example import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'drf_attempt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^examples/(?P<pk>[0-9]+)/$', views.ExampleDetail.as_view()),
    url(r'^examples/$', views.ExampleList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
