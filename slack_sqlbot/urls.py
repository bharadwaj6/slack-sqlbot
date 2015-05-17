from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slack_sqlbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sql/$', 'sqlparser.views.parse_sql')
    url(r'^admin/', include(admin.site.urls)),
)
