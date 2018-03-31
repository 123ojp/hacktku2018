from django import forms

from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = []
        fields = ('username', 'email', 'password', 'first_name','last_name', 'birthday',
                                                                 'phone',
                  'address',
                  'coler',
                  'fruit',
                  'num',
                  'constellation',
                  'gender',
                  'blood','education','score')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = []
        fields = ('username', 'email', 'password','last_name', 'first_name', 'birthday',
                                                                 'phone',
                  'address',
                  'coler',
                  'fruit',
                  'num',
                  'constellation',
                  'gender',
                  'blood','education',)
        widgets = {
            'password': forms.PasswordInput(),
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user