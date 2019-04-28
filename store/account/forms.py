from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """ Custom user registrarion form """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self):
        super().save(commit=False)

    def clean_email(self, *args, **kwargs):
        print('validating email')
        email = self.cleaned_data['email']
        user = User.objects.filter(username=email)
        if not user.exists():
            return email
        else:
            raise forms.ValidationError('Поле email должно быть уникальным')



