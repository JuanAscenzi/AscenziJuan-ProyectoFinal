from django.shortcuts import render
from AppAscenzi.models import Juguete, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "AppAscenzi/index.html")

def about(request):
    return render(request, "AppAscenzi/about.html")

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

class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("juguete-list")
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProfileUpdate(PermisoSoloDueño, UpdateView):
    model = Profile
    success_url = reverse_lazy("juguete-list")
    fields = ['avatar']

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
    
class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'


class MensajeDelete(LoginRequiredMixin, PermisoSoloDueño, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()