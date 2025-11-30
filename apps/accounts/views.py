from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from .models import AppUser
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # DEBUG: imprime en logs para ver qué llega
            print("DEBUG login attempt:", "username=", username, "password_present=", bool(password))

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # DEBUG
                print("DEBUG login success for:", username)
                return redirect('index_user')  # ajusta a tu url name real
            else:
                # añade error visible en el formulario y mensaje
                form.add_error(None, 'Usuario o contraseña incorrectos')
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            # imprime errores del formulario en logs
            print("DEBUG form errors:", form.errors)

    return render(request, 'accounts/login.html', {'form': form})


class UserListView(LoginRequiredMixin, ListView):
    login_url = 'accounts:login'
    model = AppUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    
class RegisterUserView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = AppUser(username=username, email=email)
            user.set_password(password)
            user.save()

            
            return redirect('accounts:login')
        return render(request, 'accounts/register.html', {'form': form})