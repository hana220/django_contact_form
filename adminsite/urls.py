from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
 
app_name = 'adminsite'
urlpatterns = [
    path('login/', views.AdminLogin.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('home/', login_required(views.Home.as_view()), name='home'),
    path('individual_contacts_list/', login_required(views.IndividualContactsList.as_view()), name='individual_contacts_list'),
    path('corporate_contacts_list/', login_required(views.CorporateContactsList.as_view()), name='corporate_contacts_list'),
]
