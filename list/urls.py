from django.conf.urls import url
from . import views

urlpatterns = [
    # /list/
    url(r'^$', views.index, name='index'),

    #/list/$task_id/ for details
    url(r'^(?P<task_id>[0-9]+)/$', views.detail, name='detail'),
]