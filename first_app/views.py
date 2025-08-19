from django.shortcuts import get_object_or_404, render # type: ignore
from .models import Investimento
from .forms import InvestimentoForm
from django.shortcuts import redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore


def investimentos(request):
    dados = {
        'dados': Investimento.objects.all(),
    }
    return render(request, 'investimentos/investimentos.html', dados)

def detalhe_investimento(request, id):
    investimento = Investimento.objects.get(id=id)
    return render(
        request,
        'investimentos/detalhe_investimento.html',
        {'investimento': investimento}   
    )

@login_required
def criar_investimento(request):
    if request.method == "POST":
        form = InvestimentoForm(request.POST)
        if form.is_valid():
            investimento = form.save()
            return redirect("detalhe_investimento", id=investimento.id)
        # se inválido, cai no render abaixo com erros
        contexto = {"formulario": form}
        return render(request, "investimentos/detalhe_investimento.html", contexto)

    # GET -> exibe o form vazio
    form = InvestimentoForm()
    return render(request, "investimentos/novo_investimento.html", {"formulario": form})

@login_required
def editar(request, id):
    investimento = get_object_or_404(Investimento, pk=id)
    if request.method == "POST":
        form = InvestimentoForm(request.POST, instance=investimento)
        if form.is_valid():
            form.save()
            return redirect("investimentos")
    else:
        form = InvestimentoForm(instance=investimento)

    return render(request, "investimentos/novo_investimento.html", {"formulario": form})

@login_required
def excluir(request, id):
    investimento = get_object_or_404(Investimento, pk=id)
    if request.method == "POST":
        investimento.delete()
        return redirect("investimentos")
    return render(request, "investimentos/confirmar_exclusao.html", {"investimento": investimento})







