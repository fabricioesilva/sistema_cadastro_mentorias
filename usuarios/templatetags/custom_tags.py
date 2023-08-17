from django import template
from datetime import timedelta, date
register = template.Library()


@register.filter
def extract_dict(dicio, key):
    """Método de uso no template, em que a tag retorna o valor do dicionário
        correspondente à chave passada como parâmetro.

    Args:
        dicio (Dict): Dict
        key (Str): Dict key

    Returns:
        Any: Qualquer tipo que seja value em um dicionário.
    """
    return key


@register.filter
def tempo_que_falta(data):
    falta = data - date.today()
    return falta.days


@register.filter
def matricula_ativa_filter(data):
    if data < date.today():
        return False
    else:
        return True


@register.filter
def tempo_acabando(data):
    timeuntil = data - date.today()
    if data > date.today():
        if timeuntil < timedelta(days=30):
            return True
        return False
    else:
        return False


@register.filter
def get_media_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    if len(lista) > 0:
        media = round(soma/len(lista), 2)
    else:
        media = 0
    return media


@register.filter
def set_empty(content):
    if content == None:
        return ''
    else:
        return content

@register.filter
def alternativas(alternativas, indice):
    texto = f" \
        <table class='table-small'> \
            <thead> \
            <tr> \
                <th> A </th> \
                <th> B </th>  \
                <th> C </th> \
                <th> D </th> \
                <th> E </th> \
            </tr> \
            </thead> \
            <tbody> \
                <tr> \
                    <td> {alternativas[str(indice)]['A']}% </td> \
                    <td> {alternativas[str(indice)]['B']}% </td> \
                    <td> {alternativas[str(indice)]['C']}% </td> \
                    <td> {alternativas[str(indice)]['D']}% </td> \
                    <td> {alternativas[str(indice)]['E']}% </td> \
            </tbody> \
        </table>" 
    return texto