from django import forms
from django.contrib.auth.forms import AuthenticationForm
 
class LoginAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                ("アカウントが無効です"),
                code='inactive',
            )
        if not user.is_staff:
            raise forms.ValidationError(
                ("管理者権限を持っていません"),
                code='notadmin'
            )
