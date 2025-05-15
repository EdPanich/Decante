from django import forms
from .models import Deudor, Pedido, Contacto

class DeudorForm(forms.ModelForm):
    class Meta:
        model = Deudor
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

        from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

