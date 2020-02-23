from django.urls import include, path
from . import views
from accounts.views import registration_view
from rest_framework import routers

app_name = 'accounts'

urlpatterns = [
    path('register', views.registration_view.as_view()),
]
