from django.urls import path
from . import views

urlpatterns = [
    path('deudores/', views.lista_deudores, name='lista_deudores'),
    path('deudores/<int:pk>/editar/', views.editar_deudor, name='editar_deudor'),
    path('deudores/<int:pk>/eliminar/', views.eliminar_deudor, name='eliminar_deudor'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('deudores/nuevo/', views.crear_deudor, name='crear_deudor'),

]
