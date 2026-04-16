from django import forms
from django.forms import inlineformset_factory
from .models import Pessoa, Telefone


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'idade']


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['numero']


# ADICIONADO (formset para múltiplos telefones)
TelefoneFormSet = inlineformset_factory(
    Pessoa,
    Telefone,
    form=TelefoneForm,
    extra=1,
    can_delete=True
)