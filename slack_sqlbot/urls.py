from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^sql/$', 'sqlparser.views.parse_sql'),
                       )
