from django.urls import path
from .views import *
 
app_name = 'contacts'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('individual_input/', IndividualContactInput.as_view(), name='individual_input'),
    path('individual_confirm/', IndividualContactConfirm.as_view(), name='individual_confirm'),
    path('individual_create/', IndividualContactCreate.as_view(), name='individual_create'),
    path('corporate_input/', CorporateContactInput.as_view(), name='corporate_input'),
    path('corporate_confirm/', CorporateContactConfirm.as_view(), name='corporate_confirm'),
    path('corporate_create/', CorporateContactCreate.as_view(), name='corporate_create'),
    path('form_send_complete/', FormSendComplete.as_view(), name='form_send_complete'),
]
