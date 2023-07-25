from django.shortcuts import render
from .models import Users

def home(request):
    return render(request, 'users/home.html')

def users(request):
    # Salvar os dados da tela para o banco de dados
    new_user = Users()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()

    # Exibir os usuários cadastrados em uma nova página
    users = {
        'users': Users.objects.all()
    }

    # Retornar os dados para a página de listagem

    return render(request, 'users/users.html', users)