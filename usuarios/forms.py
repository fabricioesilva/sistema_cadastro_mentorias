from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import EmailMessage
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .models import CustomUser


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    @transaction.atomic
    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def send_mail(self, uri_key, email_to=None, user=None):
        if email_to is None:
            email_to = self.cleaned_data.get('email')
            user = self.cleaned_data.get('username')
        pre_text = _(', clique no link para validar o seu email ')
        content = f"{user}{pre_text}, {settings.LOCALHOST_URL}check/email/{uri_key}"
        email = EmailMessage(
            subject=_('Bem vindo ao e-Pesquisa'),
            body=content,
            from_email=settings.NOREPLY_EMAIL,
            to=[email_to, ],
            headers={'Reply-to': settings.NOREPLY_EMAIL}
        )
        email.send()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email']
        required_fields = ['username', 'password1', 'password2', 'email']


class EditProfilerForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']


class EditUserEmailForm(forms.Form):
    email1 = forms.EmailField(label=_('Entre o novo email.'))
    email2 = forms.EmailField(label=_('Repita o novo email.'))
    password = forms.CharField(required=True,
                               label=_('Senha'),
                               widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        email1 = cleaned_data.get("email1")
        email2 = cleaned_data.get("email2")

        if email1 != email2:
            msg = _("Email preenchido deve ser igual.")
            self.add_error("email1", msg)
            self.add_error("email2", msg)
        return cleaned_data

    def send_mail(self, uri_key, email_to=None, user=None):
        pre_text = _(', clique no link para validar o seu email ')
        content = f"{user}{pre_text}, {settings.LOCALHOST_URL}check/email/{uri_key}"
        email = EmailMessage(
            subject=_('Bem vindo ao e-Pesquisa'),
            body=content,
            from_email=settings.NOREPLY_EMAIL,
            to=[email_to, ],
            headers={'Reply-to': settings.NOREPLY_EMAIL}
        )
        email.send()