from django.forms import ModelForm
from contacts.models import CorporateContact, IndividualContact
 
class IndividualContactForm(ModelForm):
    class Meta:
        model = IndividualContact
        fields = '__all__'
 
class CorporateContactForm(ModelForm):
    class Meta:
        model = CorporateContact
        fields = '__all__'
