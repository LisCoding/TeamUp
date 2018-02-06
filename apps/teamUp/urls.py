from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^/projects$', views.index),
url(r'^/login$', views.loginUser),
url(r'^/logOutUser$', views.loginUser),
url(r'^/register$', views.registerUser),
]
