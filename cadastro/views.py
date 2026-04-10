# cadastro\views.py

from django.shortcuts import redirect, render

from cadastro.forms import PessoaForm
from cadastro.models import Pessoa

def index(request):
    # Recebe todas as pessoas do banco de dados
    # pessoas = Pessoa.objects.all()

    # Recebe todas as pessoas em ordem alfabética do nome
    pessoas = Pessoa.objects.order_by('nome')

    # Total de cadastrados
    total = Pessoa.objects.count()
    
    # Dicionário que passa dados para o template
    context = {
       'pessoas': pessoas,
       'total': total,
    }
    return render(request, 'cadastro/index.html', context)

def contato(request):
    return render(request, 'cadastro/contato.html')

def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = PessoaForm()
    return render(request, 'cadastro/adicionar.html', {'form': form})