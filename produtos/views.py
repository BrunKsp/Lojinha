from django.shortcuts import render,get_object_or_404 , redirect
from .models import Produto
from django.http import HttpResponse
from .forms import ProdutoForm
from django.contrib import messages

def ListProduto (request):
    produto = Produto.objects.all()
    return render(request,'produto/ListaProd.html',{'produto':produto})


def ProdutoView (request ,id):
    produto = get_object_or_404(Produto ,pk = id)
    return render(request,'produto/produto.html',{'produto':produto})



def newProduto (request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('/')


    else:
        form = ProdutoForm()
        return render(request,'produto/addproduto.html',{'form':form})


def EditProduto (request,id):
    produto = get_object_or_404(Produto ,pk = id)
    form = ProdutoForm(instance= produto)


    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produto)
        if (form.is_valid()):
            produto.save()
            return redirect('/')
        else :
            return render(request,'produto/editproduto.html',{'form':form, 'produto':produto})


    else:
        return render(request,'produto/editproduto.html',{'form':form, 'produto':produto})


def DeleteProduto (request ,id):
    produto = get_object_or_404(Produto ,pk = id)
    produto.delete()

    messages.info(request,'Tarefa Delatada com Sucesso')
    return redirect('/')

    
