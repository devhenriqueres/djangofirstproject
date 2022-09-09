from ast import If
from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render
from django.shortcuts import get_object_or_404 # busca o objeto ou retorne pag não encontrada
import os
from core.models import Produto
from django.http import HttpResponse
from django.template import loader


def index(request):

    produtos = Produto.objects.all()

    context = {
        'curso': 'django',
        'descricao': 'Venda de produtos',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod =get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
