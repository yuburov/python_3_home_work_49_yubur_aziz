from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import Profile


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Username')
    first_name = forms.CharField(max_length=100, required=False, label='First name')
    last_name = forms.CharField(max_length=100, required=False, label='Last name')
    password = forms.CharField(max_length=100, required=True, label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password confirm',
                                       widget=forms.PasswordInput)
    email = forms.EmailField(required=True, label='Email')

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if password_1 != password_2:
            raise ValidationError('Passwords do not match',
                                  code='passwords_do_not_match')
        if not first_name and not last_name:
            raise ValidationError('Please fill in one of this fields: first name, last name',
                                  code='empty field')
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists',
                                  code='user_email_exists')
        except User.DoesNotExist:
            return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists',
                                  code='user_username_exists')
        except User.DoesNotExist:
            return username

class UserChangeForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', required=False)
    about_me = forms.CharField(max_length=3000,label='О себе', required=False, widget=forms.Textarea)
    github_profile = forms.URLField(label='Профиль на GitHub', required=False)

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        user = super().save(commit=commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile = Profile.objects.get_or_create(user=self.instance)[0]
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data.get(field))
        if not profile.avatar:
            profile.avatar = None
        if commit:
            profile.save()


    def clean_github_profile(self):
        github_profile = self.cleaned_data.get('github_profile')
        if not github_profile.startswith('http://github.com/') and github_profile is not '':
            raise ValidationError('profile address is incorrect', code='wrong address')
        return github_profile


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'about_me', 'github_profile']
        profile_fields = ['avatar', 'about_me', 'github_profile']

class UserChangePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=100, required=True, label='New password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password confirm',
                                       widget=forms.PasswordInput)
    old_password = forms.CharField(max_length=100, required=True, label='Old password', widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_confirm']
        if password_1 != password_2:
            raise ValidationError('Passwords do not match',
                                  code='passwords_do_not_match')
        return self.cleaned_data

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invailid password', code='Invalid password')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']

