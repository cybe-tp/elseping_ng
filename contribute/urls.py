from django.conf.urls import url
from . import views

urlpatterns = [
    # /list/
    url(r'^$', views.index, name='index'),

]