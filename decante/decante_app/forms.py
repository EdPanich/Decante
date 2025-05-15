from django import forms
from .models import Deudor, Pedido

class DeudorForm(forms.ModelForm):
    class Meta:
        model = Deudor
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
