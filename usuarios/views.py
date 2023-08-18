# from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime
from utils.resources import POLICY_LANGUAGES, check_user_is_regular
from usuarios.models import (
    CustomUser, UserEmailCheck, Preferences, DeletedUser
)
from politicas.models import PolicyAcepted, PolicyRules
from .forms import (
    CustomUserForm,
    EditProfilerForm,
    EditUserEmailForm,
    EditPreferencesForm,
    ConfirmPasswordForm
)
from mentorias.models import Mentoria, MatriculaAlunoMentoria


# Create your views here.
def index_view(request):
    return render(request, 'usuarios/index.html', {})


def home_view(request):
    if request.user.is_authenticated:
        preference = request.user.preferences.login_redirect
        if request.user.preferences.login_redirect == 1:
            return redirect('usuarios:home_student')
        elif preference == 2:
            return redirect('usuarios:home_mentor')
        else:
            return render(request, 'usuarios/home.html', {})
    else:
        return redirect(request, 'usuarios:index')


@method_decorator([login_required], name='dispatch')
class HomeMentorView(TemplateView):
    template_name = 'usuarios/home_mentor.html'

    def get_context_data(self, **kwargs):
        # from django.db.models import Prefetch
        # mentorias = Mentoria.objects.filter(mentor=self.request.user).prefetch_related(
        #     Prefetch('matriculas', queryset=MatriculaAlunoMentoria.objects.filter(encerra_em__gte=date.today())))
        mentorias = Mentoria.objects.filter(mentor=self.request.user)
        context = super().get_context_data(**kwargs)
        queryset = MatriculaAlunoMentoria.objects.none()
        # aplicacoes
        context['ajudo'] = 'ajudo'
        # for mentoria in mentorias:
        #     queryset |= mentoria.matriculas.filter(encerra_em__gte=date.today())
        # context['matriculas'] = queryset
        context['mentorias'] = mentorias
        return context


@method_decorator([login_required], name='dispatch')
class HomeStudentView(View):
    template_name = 'usuarios/home_student.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('default') == 'estudante':
            request.user.preferences.login_redirect = 1
            request.user.preferences.save()
        if request.user.is_anonymous:
            return redirect('usuarios:index')
        if check_user_is_regular(request):
            return render(request, self.template_name)
        else:
            logout(request)
            messages.error(request, _('Ops! Usuário não encontrado!'))
            return redirect('login')


class CadastroView(CreateView):
    form_class = CustomUserForm
    template_name = 'usuarios/cadastro.html'
    success_url = 'login'

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if self.request.LANGUAGE_CODE in POLICY_LANGUAGES:
                user.policy_lang = self.request.LANGUAGE_CODE
            else:
                user.policy_lang = 'pt'

            user.save()
            PolicyAcepted.objects.create(
                user=user,
                policy=PolicyRules.objects.get(
                    language=user.policy_lang, active=True)
            )
            check_user = UserEmailCheck.objects.create(
                user=user,
            )
            try:
                form.send_mail(check_user.uri_key)
            except BadHeaderError:
                print("Erro ao enviar o email.")
            messages.success(self.request,
                             _('Foi enviado um link para confirmação do seu email!'))

        return redirect('usuarios:index')


def user_logout(request):
    logout(request)
    return redirect('usuarios:cadastro')

def check_user_email(request, uri_key):
    if request.method == 'GET':
        ck_user = UserEmailCheck.objects.filter(
            uri_key=uri_key
        ).first()
        if ck_user:
            user = ck_user.user
            if user:
                user.email_checked = True
                user.save()
                ck_user.save()
                ck_user.confirmed = datetime.now()
                ck_user.save()
                logout(request)
                messages.success(request, _('Email confirmado com sucesso!'))
                return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('usuarios:index')


def change_password_method(request):
    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect('login')
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            logout(request)
            messages.success(
                request, _('Senha alterada com sucesso!'))
            return redirect('login')
        else:
            messages.error(request, _('Reveja o formulário!'))
    else:
        if request.user.is_anonymous:
            return redirect('login')
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/change_password.html', {
        'form': form
    })


@method_decorator([login_required], name='dispatch')
class ProfileView(View):
    template_name = 'usuarios/profile_view.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


@method_decorator([login_required], name='dispatch')
class EditPreferencesView(UpdateView):
    model = Preferences
    template_name = 'usuarios/edit_preferences.html'
    form_class = EditPreferencesForm
    success_url = reverse_lazy('usuarios:profile_view')


@method_decorator([login_required], name='dispatch')
class EditProfileView(UpdateView):
    form_class = EditProfilerForm
    model = CustomUser
    template_name = 'usuarios/edit_profile.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = EditProfilerForm(instance=self.request.user)
        return ctx


def edit_user_email(request):
    if request.method == 'POST':
        password = request.POST['password']
        email1 = request.POST['email1']
        senha_correta = request.user.check_password(password)
        if not senha_correta:
            messages.error(request, _('Senha incorreta!'))
            form = EditUserEmailForm(request.POST)
            return render(request, 'usuarios/edit_user_email.html', {'form': form})
        elif CustomUser.objects.filter(email=email1).exists():
            messages.error(request, 'Email já existe.')
            form = EditUserEmailForm(request.POST)
            return render(request, 'usuarios/edit_user_email.html', {'form': form})
        else:
            form = EditUserEmailForm(request.POST)
            request.user.email_checked = False
            request.user.email = email1
            request.user.save()
            check_user = UserEmailCheck.objects.create(
                user=request.user,
            )
            try:
                form.send_mail(check_user.uri_key, email_to=email1, user=request.user)
            except BadHeaderError:
                print("Erro ao enviar o email.")
            logout(request)
            messages.success(request,
                             _('Foi enviado um link para confirmação do seu email!'))
            return redirect('usuarios:index')
    form = EditUserEmailForm(request.POST or None)
    return render(request, 'usuarios/edit_user_email.html', {'form': form})


def delete_user(request, username):
    if request.method == 'GET':
        if username != request.user.username:
            messages.error(request, _('Usuário inválido!'))
            return redirect('usuarios:index')
        context = {'form': ConfirmPasswordForm(
            request.POST or None, instance=request.user), }
        return render(request, 'usuarios/check_password.html',
                      context)

    if request.method == 'POST':
        if username != request.user.username:
            messages.error(request, _('Usuário inválido!'))
            return redirect('usuarios:index')
        form = ConfirmPasswordForm(request.POST, instance=request.user)
        if form.is_valid():
            DeletedUser.objects.create(
                user_id=request.user.id,
                email=request.user.email,
                user_since=request.user.user_since
            )
            request.user.delete()
            messages.add_message(request, messages.SUCCESS,
                                 _('Perfil removido.'))
            return redirect('usuarios:index')
        else:
            messages.add_message(request, messages.ERROR,
                                 _('Erro na digitação da senha.'))
            form = ConfirmPasswordForm()
            return render(request, 'usuarios/check_password.html',
                          {"form": form})
