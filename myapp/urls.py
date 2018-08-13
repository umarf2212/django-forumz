from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.hello, name='hello'),
	url(r'article/(\d+)/', views.article, name='article'),
	url(r'name/', views.hello2, name='hello2'),
	url(r'crud/', views.crudops, name='crudops'),
	url(r'connection/', TemplateView.as_view(template_name = 'login.html')),
	url(r'^login/', views.login, name='login'),
]