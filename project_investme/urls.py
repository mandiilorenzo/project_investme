from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from first_app import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('novo_investimento/', views.criar_investimento, name='novo_investimento'),
    path('<int:id>/', views.detalhe_investimento, name='detalhe_investimento'),
    path('', views.investimentos, name='investimentos'),
    path('novo_investimento/<int:id>', views.editar, name='editar_investimento'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
]
