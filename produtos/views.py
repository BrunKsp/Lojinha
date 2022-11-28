from django.shortcuts import render,get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages


class ProdutoView():
    def listaProd (request):
        
        search = request.GET.get('search')

        if search :
            produtos = Produto.objects.filter(name_icontains=search)
        else :
            produtos = Produto.objects.all()
            return render(request,'produto/ListaProd.html',{'produto':produtos})


    def produtoView (request ,id):
        produto = get_object_or_404(Produto ,pk=id)
        return render(request,'produto/produto.html',{'produto':produto})



    @login_required
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

    @login_required
    def editProduto (request,id):
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

    @login_required
    def deleteProduto (request ,id):
        produtos = get_object_or_404(Produto ,pk = id)
        produtos.delete()

        messages.info(request,'Tarefa Deletada com Sucesso')
        return redirect('/')


    def sobreNos (request) :

        if request.method == 'GET':
            return render(request,'sobrenos.html')
    
