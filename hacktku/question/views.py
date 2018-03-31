from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from .models import UserProfile
from .serializers import UserProfileSerializer, QuestionSerializer

from rest_framework import viewsets
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = QuestionSerializer