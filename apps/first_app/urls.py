from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/',views.new),
    url(r'^create/',views.create),
    url(r'^(?P<num>\d+)$',views.number),
    url(r'^(?P<num>\d+)/edit$',views.edit), #DONT FORGET THE STUPUD COMMA!!
    url(r'^(?P<num>\d+)/delete$',views.delete),
]