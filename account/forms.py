from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import authenticate 
import captcha
import  captcha.helpers
from captcha.fields import CaptchaField


from account.models import Account

class CaptchaTestForm(forms.Form):
    
    captcha = CaptchaField(generator=captcha.helpers.math_challenge)

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=255,help_text="REQUIERD")
    
    class Meta:
        model=Account
        fields = ('email', 'username', 'password1', 'password2',)
    
    
    
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        try:
            account=Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email{email} is already in use.')
    
    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            account=Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError(f'Username{username} is already in use.')

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ('email', 'password')
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('username','email','hide_email','profile_image')
        def clean_username(self):
            username=self.cleaned_data['username']
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError(f'Username{username} is already in use.')
        def clean_email(self):
            email=self.cleaned_data['email'].lower()
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError(f'Email{email} is already in use.')
        def save(self,commit=True):
            account=super(AccountUpdateForm,self).save(commit=False)
            account.username=self.cleaned_data['username']
            account.email=self.cleaned_data['email']
            account.hide_email=self.cleaned_data['hide_email']
            account.profile_image = self.cleaned_data['profile_image']
            if commit:
                account.save()
            return account


#https://stackoverflow.com/questions/53218535/is-it-possible-to-do-a-private-chat-with-django-channels