
from django.urls import path 
from . import views


urlpatterns = [
    path('',views.listaProd,name = "produto-list"),
    path('produto/<int:id>',views.produtoView,name = "produto-view"),
    path('newproduto/', views.newProduto, name="new-produto"),
    path('edit/<int:id>',views.editProduto,name = "edit-produto"),
    path('delete/<int:id>',views.deleteProduto,name = "delete-produto"),
    path('sobrenos/',views.sobreNos ,name= "sobre-nos"),
    
]