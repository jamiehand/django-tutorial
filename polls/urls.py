# URLconf for polls

from django.conf.urls import url

from . import views

urlpatterns = [  # Wire views into polls.urls module by adding url() calls.
    # Note: "1st" notes indicate the code I had before amending to generic views in tutorial 4.
    # Note: The 'r' in front of each regular expression string is optional but recommended. It tells Python that a
    # string is raw - that nothing in the string should be escaped.

    # ex: /polls/
    # 1st: url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag in polls/index.html
    # added 'specifics' to make it, e.g., polls/specifics/5
    # Note: ?P<question_id> defines the name that will be used to identify the matched pattern
    # 1st: url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),   # this code lets Dj identify the page
                                                                              # (view) to send, based on the URL.
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    # 1st: url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    # 1st: url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
