from django.urls import path
from . import views

app_name = '{% templatetag openvariable %}app_name{% templatetag closevariable %}'

urlpatterns = [
    path('', views.main, name='main'),
]