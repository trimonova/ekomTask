from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_form/', views.parse_request),
]
