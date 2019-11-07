from django.conf.urls import url
from . import views

app_name = "mailing_ns"

urlpatterns = [
    url(r'^$', views.mailing, name="mailing"),
]