from django.conf.urls import patterns, include, url



urlpatterns = patterns('mysite.content.views',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
	url(r'^index/$', 'index', name='index'),
    url(r'^(?P<id>[0-9]{0,5})/', 'content',name='get_content'),
    url(r'^level_1/(?P<id>[0-9]{0,5})/', 'level_1',name='level_1'),
    # url(r'^(?P<types>psg)/level_1/(?P<id>[0-9]{0,5})/', 'level_1',name='level_1'),
    url(r'^level_2/(?P<id>[0-9]{0,5})/', 'level_2',name='level_2'),
    url(r'^topmenu/(?P<id>[0-9]{0,5})/', 'topmenu',name='topmenu'),
    url(r'^footer/', 'footer', name='footer'),

)
