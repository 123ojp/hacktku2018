from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .form import UserForm, SignUpForm
from .models import UserProfile
from .serializers import UserProfileSerializer, QuestionSerializer

from django.shortcuts import get_object_or_404,redirect, render



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

    # def form_valid(self, form, **kwargs):
    #     self.object = form.save(commit=False)
    #     self.object.set_password(self.object.password)
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

class UserList(generic.ListView):
    model = UserProfile
    template_name = 'user/dashboard.html'

def index(request):
    return render(request, 'index.html')

from django.contrib.auth.decorators import login_required

@login_required
def game(request):
    return render(request, 'game.html')



class UserDetail(generic.DetailView):
    model = UserProfile
    template_name = 'user/score.html'



def UserDetail_update(request, id,newscore):
    obj = get_object_or_404(UserProfile, id=id)
    obj.score = newscore
    obj.save(update_fields=["score"])
    messages.success(request, '已購買')
    return redirect('index')