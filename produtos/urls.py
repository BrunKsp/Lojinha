
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.ListProduto,name = "produto-list"),
    path('produto/<int:id>',views.ProdutoView,name = "produto-view"),
    path('newproduto/', views.newProduto, name="new-produto"),
    path('edit/<int:id>',views.EditProduto,name = "edit-produto"),
    path('delete/<int:id>',views.DeleteProduto,name = "delete-produto"),

]