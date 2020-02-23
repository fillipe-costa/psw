from django.shortcuts import render
from accounts.serializers import RegistrationSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.

class registration_view(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegistrationSerializer
