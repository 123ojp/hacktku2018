from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .form import UserForm, SignUpForm
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

class SignUp(generic.CreateView):
    model = UserProfile
    form_class = SignUpForm
    template_name = 'user/form.html'

    def get_success_url(self):
        messages.success(self.request, '註冊成功')
        return reverse('index')

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UserList(generic.ListView):
    model = UserProfile
    template_name = 'user/dashboard.html'

def index(request):
    return render(request, 'index.html')
