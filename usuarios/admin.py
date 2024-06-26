from django.contrib import admin, messages
from datetime import date, timedelta
from .models import CustomUser, UserEmailCheck, Preferences, DeletedUser, PerfilCobranca
from assinaturas.models import AssinaturasMentor, OfertasPlanos


@admin.action(description="Contrata assinatura com novo plano para geral")
def contrata_assinatura_geral(modeladmin, request, queryset):
    hoje = date.today()
    ontem = date.today() - timedelta(days=1) 
    amanha = date.today() + timedelta(days=1) 
    oferta_disponivel = OfertasPlanos.objects.filter(encerra_em__gte=ontem, promocional=True).exclude(inicia_vigencia__gte=amanha).first()    
    if not oferta_disponivel:
        oferta_disponivel = OfertasPlanos.objects.filter(encerra_em__gte=ontem, promocional=False).exclude(inicia_vigencia__gte=amanha).first()
    if not oferta_disponivel:
        messages.error(request, "Erro ao encontrar oferta! Tente novamente mais tarde.")
        return
    for mentor in queryset:
        data_atual = date.today()
        inicio_mes_atual = data_atual.replace(day=1) 
        mes_anterior = inicio_mes_atual - timedelta(days=1)
        inicio_mes_anterior = mes_anterior.replace(day=1)
        assinatura = AssinaturasMentor.objects.filter(mentor=mentor, encerra_em__gte=inicio_mes_anterior).exclude(inicia_vigencia__gte=inicio_mes_anterior).first()
        if not assinatura:
            assinatura = AssinaturasMentor.objects.filter(mentor=mentor).filter(criada_em__gte=inicio_mes_anterior).first()
        hoje = date.today()
        if not assinatura:            
            AssinaturasMentor.objects.create(
            mentor=mentor,
            oferta_contratada=oferta_disponivel,
            inicia_vigencia=date.today(),
            encerra_em=date(year=hoje.year+1, month=hoje.month, day=28)
            )
        else:
            sessenta_dias_adiante = date.today() + timedelta(days=60)
            encerramento_matricula = assinatura.encerra_em
            if encerramento_matricula > sessenta_dias_adiante:                
                continue
            else:
                AssinaturasMentor.objects.create(
                    mentor=mentor,
                    oferta_contratada=oferta_disponivel,
                    inicia_vigencia=encerramento_matricula+timedelta(days=1),
                    encerra_em=date(year=encerramento_matricula.year+1, month=encerramento_matricula.month, day=28)
                )
       

class CustomUserAdmin(admin.ModelAdmin):
    actions=[contrata_assinatura_geral]
    list_display = ('pk', 'username', 'email', 'email_checked', 'user_since')

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserEmailCheck)
admin.site.register(Preferences)
admin.site.register(DeletedUser)
admin.site.register(PerfilCobranca)
