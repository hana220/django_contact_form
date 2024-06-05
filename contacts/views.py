from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import CorporateContactForm, IndividualContactForm
from .models import IndividualContact, CorporateContact
 
class Home(generic.TemplateView):
    template_name = 'contacts/index.html'
 
 
class IndividualContactInput(generic.FormView):
    template_name = 'contacts/individual_contact_input.html'
    form_class = IndividualContactForm
 
    def form_valid(self, form):
        return render(self.request, IndividualContactInput.template_name, {'form': form})
 
 
class IndividualContactConfirm(generic.FormView):
    form_class = IndividualContactForm
 
    def form_valid(self, form):
        return render(self.request, 'contacts/individual_contact_confirm.html', {'form': form})
 
    def form_invalid(self, form):
        return render(self.request, IndividualContactInput.template_name, {'form': form})
 
 
class IndividualContactCreate(generic.CreateView):
    form_class = IndividualContactForm
    success_url = reverse_lazy('contacts:form_send_complete')
 
    def form_invalid(self, form):
        return render(self.request, IndividualContactInput.template_name, {'form': form})
 
    def form_valid(self, form):
        IndividualContact.email_users(form, 'sample@internetacademy.co.jp')
        return super().form_valid(form)
 
 
class CorporateContactInput(generic.FormView):
    template_name = 'contacts/corporate_contact_input.html'
    form_class = CorporateContactForm
 
    def form_valid(self, form):
        return render(self.request, CorporateContactInput.template_name, {'form': form})
 
 
class CorporateContactConfirm(generic.FormView):
    form_class = CorporateContactForm
 
    def form_valid(self, form):
        return render(self.request, 'contacts/corporate_contact_conﬁrm.html', {'form': form})
 
    def form_invalid(self, form):
        return render(self.request, CorporateContactInput.template_name, {'form': form})
 
 
class CorporateContactCreate(generic.CreateView):
    form_class = CorporateContactForm
    success_url = reverse_lazy('contacts:form_send_complete')
 
    def form_invalid(self, form):
        return render(self.request, CorporateContactInput.template_name, {'form': form})
 
    def form_valid(self, form):
        CorporateContact.email_users(form, 'sample@internetacademy.co.jp')
        return super().form_valid(form)
 
 
class FormSendComplete(generic.TemplateView):
    template_name = 'contacts/form_send_complete.html'
