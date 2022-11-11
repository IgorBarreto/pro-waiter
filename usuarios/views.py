from django.contrib.auth.views import LoginView

# Create your views here.
class LoginUsuario(LoginView):
    template_name = "usuarios/entrar.html"
