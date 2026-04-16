# cadastro\views.py

from django.shortcuts import get_object_or_404, redirect, render
from cadastro.forms import PessoaForm, TelefoneFormSet
from cadastro.models import Pessoa
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    pessoas = Pessoa.objects.order_by('nome')
    total = Pessoa.objects.count()

    context = {
        'pessoas': pessoas,
        'total': total,
    }
    return render(request, 'cadastro/index.html', context)


def contato(request):
    return render(request, 'cadastro/contato.html')


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        formset = TelefoneFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            pessoa = form.save()
            formset.instance = pessoa
            formset.save()

            messages.success(request, 'Pessoa adicionada com sucesso!')
            return redirect('index')
    else:
        form = PessoaForm()
        formset = TelefoneFormSet()

    return render(request, 'cadastro/adicionar.html', {
        'form': form,
        'formset': formset
    })


def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'cadastro/detalhe.html', {'pessoa': pessoa})


@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        formset = TelefoneFormSet(request.POST, instance=pessoa)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()

            messages.success(request, f'{pessoa.nome} atualizada com sucesso!')
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
        formset = TelefoneFormSet(instance=pessoa)

    return render(request, 'cadastro/editar.html', {
        'form': form,
        'formset': formset,
        'pessoa': pessoa
    })


@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Pessoa apagada com sucesso!')
        return redirect('index')        
    return render(request, 'cadastro/deletar.html', {'pessoa': pessoa})