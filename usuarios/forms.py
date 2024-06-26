from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.mail import EmailMessage
from django.db import transaction
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .models import CustomUser, Preferences, PerfilCobranca
import threading
from utils.resources import valida_cpf


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome_apresentacao = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':_("Prof. Silva")})
    )

    @transaction.atomic
    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def thread_email(self, uri_key, email_to=None, user=None, politica_aceita=None, termo_aceito=None):
        email_template_name = "usuarios/validacao_email.txt"
        c = {
            'site_name': settings.SITE_NAME,
            'user_email': email_to,
            'url':  f'{settings.LOCALHOST_URL}/check/email/{uri_key}'
        }
        mensagem_email = render_to_string(email_template_name, c)
        email = EmailMessage(
            subject=_(f'Valide seu email no { settings.SITE_NAME }'),
            body=mensagem_email,
            from_email=settings.NOREPLY_EMAIL,
            to=[email_to, ],
            headers={'Reply-to': settings.NOREPLY_EMAIL}, 
            attachments=[
                    (politica_aceita.policy.title, politica_aceita.policy.arquivo_politica.read(), 'application/pdf'),
                    (termo_aceito.termo.termo_title, termo_aceito.termo.arquivo_termo.read(), 'application/pdf')
                ]
        )
        email.send()

    def send_mail(self, uri_key, email_to=None, user=None, politica=None, termo=None):
        if email_to is None:
            email_to = self.cleaned_data.get('email')
            user = self.cleaned_data.get('username')    
        mailing_thread = threading.Thread(
            target=self.thread_email,
            args=(uri_key, email_to, user, politica, termo)
        )
        mailing_thread.start()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'nome_apresentacao', 'username', 'email', 'password1', 'password2']


class EditProfilerForm(forms.ModelForm):
    cpf_usuario = forms.CharField(
        max_length=11,
        label=_('CPF'),
        required=False
    )

    def clean(self):
        super(EditProfilerForm, self).clean()
        if len(self.cleaned_data['cpf_usuario']) > 0:
            if not valida_cpf(self.cleaned_data.get('cpf_usuario')):
                self.add_error('cpf_usuario', _('CPF inválido.'))
        return self.cleaned_data
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'nome_apresentacao', 'username', 'cpf_usuario']


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
    
    def thread_email(self, user, uri_key, email_to):
        pre_text = _(', clique no link para validar o seu email ')
        content = f"{user}{pre_text}, {settings.LOCALHOST_URL}check/email/{uri_key}"
        email = EmailMessage(
            subject=_('Bem vindo'),
            body=content,
            from_email=settings.NOREPLY_EMAIL,
            to=[email_to, ],
            headers={'Reply-to': settings.NOREPLY_EMAIL}
        )       
        email.send()

    def send_mail(self, uri_key, email_to=None, user=None):
        mailing_thread = threading.Thread(
            target=self.thread_email,
            args=(user, uri_key, email_to)
        )
        mailing_thread.start()            


class EditPreferencesForm(forms.ModelForm):
    ROLE_CHOICES = (
        (1, 'Estudante'),
        (2, 'Mentor'),
        (3, 'Sempre perguntar'),
    )
    login_redirect = forms.ChoiceField(
        label=_('Após login, ir direto para a ferramenta escolhida:'),
        help_text=_('Escolha uma opção para ir direto ao painel quando fizer o login.'),
        widget=forms.RadioSelect(
            attrs={'class': 'radio-input'}
        ),
        choices=ROLE_CHOICES,
    )

    class Meta:
        model = Preferences
        fields = ['login_redirect']


class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label=_('Confirme a senha'),
        widget=forms.PasswordInput(attrs={'type': 'password'})
    )

    class Meta:
        model = CustomUser
        fields = ('confirm_password', )

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not self.instance.check_password(confirm_password):
            # Password does not match.
            self.add_error('confirm_password', _('Senha não confere.'))

    def save(self, commit=True):
        return super(ConfirmPasswordForm, self).save(commit)

class PerfilCobrancaForm(forms.ModelForm):
    telefone1 = forms.CharField(
        label="Telefone 1*",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '(11) 98989999 '})
    )
    telefone2 = forms.CharField(
        label="Telefone 2",
        required=False,        
        widget=forms.TextInput(attrs={'placeholder': '(11) 98989999'})
    )
    cpf_cnpj = forms.CharField(
        required=False,
        label=_("Informe o CPF"),        
    )
    # password1 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput()
    # )
    # password2 = forms.CharField(
    #     required=True,
    #     widget=forms.PasswordInput()
    # )
    class Meta:
        model = PerfilCobranca
        fields =  ['telefone1', 'telefone2', 'cpf_cnpj']
