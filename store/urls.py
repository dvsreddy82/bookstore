from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.store,name='index'),
    url(r'^count/',views.count,name='count'),

]