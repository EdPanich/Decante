from django.urls import path
from . import views, registro

urlpatterns = [
    path('deudores/', views.lista_deudores, name='lista_deudores'),
    path('deudores/<int:pk>/editar/', views.editar_deudor, name='editar_deudor'),
    path('deudores/<int:pk>/eliminar/', views.eliminar_deudor, name='eliminar_deudor'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('deudores/nuevo/', views.crear_deudor, name='crear_deudor'),
    path('contactos/', views.lista_contactos, name='lista_contactos'),
    path('contactos/nuevo/', views.crear_contacto, name='crear_contacto'),
    path('contactos/<int:pk>/editar/', views.editar_contacto, name='editar_contacto'),
    path('contactos/<int:pk>/eliminar/', views.eliminar_contacto, name='eliminar_contacto'),
    path('contactos/importar-vcf/', views.importar_contactos_vcf, name='importar_contactos_vcf'),
    path('deudores/seleccionar-contacto/', views.seleccionar_contacto_para_deudor, name='seleccionar_contacto_para_deudor'),
    path('cobrar/', views.cobrar, name='cobrar'),



]
