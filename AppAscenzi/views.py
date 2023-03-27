from django.shortcuts import render
from AppAscenzi.models import Juguete
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "AppAscenzi/index.html")

class JugueteList(ListView):
    model = Juguete
    context_object_name = "juguetes"

class JugueteDetail(DetailView):
    model = Juguete
    context_object_name = "juguete"

class JugueteUpdate(LoginRequiredMixin, UpdateView):
    model = Juguete
    success_url = reverse_lazy("juguete-list")
    fields = '__all__'

class JugueteDelete(LoginRequiredMixin, DeleteView):
    model = Juguete
    success_url = reverse_lazy("juguete-list")

class JugueteCreate(LoginRequiredMixin, CreateView):
    model = Juguete
    success_url = reverse_lazy("juguete-list")
    fields = '__all__'

class JugueteSearch(ListView):
    model = Juguete
    context_object_name = "juguetes"
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Juguete.objects.filter(nombre__icontains=criterio).all()
        return result
    
class Login(LoginView):
    next_page = reverse_lazy("juguete-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("juguete-list")

class Logout(LogoutView):
    next_page = reverse_lazy('index')

