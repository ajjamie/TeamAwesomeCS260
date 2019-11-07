from django.conf.urls import url
#from django.urls import path
from . import views

app_name = "api_ns"

urlpatterns = [
    url(r'^$', views.api, name="api"),
]