from django.contrib.auth import views
from django.views import generic
from .forms import LoginAuthenticationForm
from contacts.models import IndividualContact, CorporateContact
 
class AdminLogin(views.LoginView):
    template_name = 'adminsite/login.html'
    authentication_form = LoginAuthenticationForm
 
class Logout(views.LogoutView):
    next_page = '/adminsite/login'
 
class Home(views.TemplateView):
    template_name = 'adminsite/home.html'
 
class IndividualContactsList(generic.ListView):
    model = IndividualContact
    template_name = 'adminsite/individual_contacts_list.html'
 
class CorporateContactsList(generic.ListView):
    model = CorporateContact
    template_name = 'adminsite/corporate_contacts_list.html'
