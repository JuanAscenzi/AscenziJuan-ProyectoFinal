from django.shortcuts import render
from AppAscenzi.models import Juguete
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "AppAscenzi/index.html")

class JugueteList(ListView):
    model = Juguete
    context_object_name = "juguetes"

class JugueteMineList(LoginRequiredMixin, JugueteList):

    def get_queryset(self):
        return Juguete.objects.filter(publisher=self.request.user.id).all()

class JugueteDetail(DetailView):
    model = Juguete
    context_object_name = "juguete"

class PermisoSoloDueño(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Juguete.objects.filter(publisher=user_id, id=post_id).exists()

class JugueteUpdate(LoginRequiredMixin,PermisoSoloDueño, UpdateView):
    model = Juguete
    success_url = reverse_lazy("juguete-list")
    fields = '__all__'


class JugueteDelete(LoginRequiredMixin,PermisoSoloDueño, DeleteView):
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

