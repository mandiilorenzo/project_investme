from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()                 
            login(request, user)                
            messages.success(request, f'Conta criada para {user.username}!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados e tente novamente.')
            return render(request, 'users/registrar.html', {'formulario': form})  # reexibe com erros
    else:
        form = UserRegisterForm()
        return render(request, 'users/registrar.html', {'formulario': form})

        
