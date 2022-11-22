from django.shortcuts import render,get_object_or_404 , redirect
from .models import Produto
from django.http import HttpResponse
from .forms import ProdutoForm
from django.contrib import messages
from django.core.paginator import Paginator

def ListaProd (request):
    
    produtos = Produto.objects.all()
    paginator = Paginator(produtos,10)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    return render(request,'produto/ListaProd.html',{'produto':produtos})


def ProdutoView (request ,id):
    produtos = get_object_or_404(Produto ,pk = id)
    return render(request,'produto/produto.html',{'produto':produtos})



def newProduto (request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produtos = form.save(commit=False)
            produtos.save()
            return redirect('/')


    else:
        form = ProdutoForm()
        return render(request,'produto/addproduto.html',{'form':form})


def EditProduto (request,id):
    produtos = get_object_or_404(Produto ,pk = id)
    form = ProdutoForm(instance= produtos)


    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produtos)
        if (form.is_valid()):
            produtos.save()
            return redirect('/')
        else :
            return render(request,'produto/editproduto.html',{'form':form, 'produto':produtos})


    else:
        return render(request,'produto/editproduto.html',{'form':form, 'produto':produtos})


def DeleteProduto (request ,id):
    produtos = get_object_or_404(Produto ,pk = id)
    produtos.delete()

    messages.info(request,'Tarefa Delatada com Sucesso')
    return redirect('/')

    
