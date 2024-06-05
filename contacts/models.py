from django.db import models
from django.template.loader import get_template
from accounts.models import CustomUser
 
def contact_type_handler(contact_type):
    if not isinstance(contact_type, str):
        raise TypeError("contact_type must be str type")
 
    if contact_type not in ('individual', 'corporate'):
        raise ValueError("contact_type must be 'individual' or 'corporate'")
 
 
class BaseContact(models.Model):
    datetime = models.DateTimeField(verbose_name='お問合せ日時', auto_now_add=True)
    content = models.TextField(verbose_name='お問合せ内容', blank=False)
    email = models.EmailField(verbose_name='メールアドレス', blank=False)
 
    class Meta:
        abstract = True
 
    def __str__(self):
        return self.content
 
    @staticmethod
    def base_email_users(form, from_email, contact_type):
        contact_type_handler(contact_type)
        context = {
            'form': form,
        }
        subject_template = get_template('contacts/email/{}_subject.txt'.format(contact_type))
        subject = subject_template.render(context)
 
        message_template = get_template('contacts/email/{}_message.txt'.format(contact_type))
        message = message_template.render(context)
 
        CustomUser.email_users(CustomUser.get_users_emailed(), subject, message, from_email)

class IndividualContact(BaseContact):
    fullname = models.CharField(verbose_name='氏名', blank=False, max_length=30)
    kana = models.CharField(verbose_name='フリガナ', blank=False, max_length=60)
 
    @staticmethod
    def email_users(form, from_email):
        BaseContact.base_email_users(form, from_email, 'individual')
 
 
class CorporateContact(BaseContact):
    corporate_name = models.CharField(verbose_name='企業名', blank=False, max_length=30)
    pic_name = models.CharField(verbose_name='担当者名', blank=False, max_length=30)
    phonenumber = models.CharField(verbose_name='電話番号', blank=False, max_length=16)
 
    @staticmethod
    def email_users(form, from_email):
        BaseContact.base_email_users(form, from_email, 'corporate')
