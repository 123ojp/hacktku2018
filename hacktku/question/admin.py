from django.contrib import admin
from django import forms
# Register your models here.
from .models import Question, UserProfile, Readquestion
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

admin.site.register(Question)
admin.site.register(Readquestion)


class UserProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile


class UserProfileAdmin(UserAdmin):
    form = UserProfileForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'birthday',
            'phone',
            'address',
            'coler',
            'fruit',
            'num',
            'constellation',
            'gender',
            'blood',
            'education','score',)}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
