from .models import User
from django import forms



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "UserName",
            "PW",
        ]
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs.update({"class" : "account-input login-input"})
            self.fields["UserName"].widget.attrs.update({"placeholder" : "username"})
            self.fields["PW"].widget.attrs.update({"placeholder" : "password"})
        

class SignUpForm(forms.Form):
    UserName = forms.CharField(max_length=20)
    Email = forms.EmailField( label = "")
    PW1 = forms.CharField(widget = forms.PasswordInput, label = "")
    PW2 = forms.CharField(widget = forms.PasswordInput, label = "")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False
            self.fields["UserName"].widget.attrs.update({"placeholder" : "user name", "autocomplete" : "false", "class" : "account-input username-input"})
            self.fields["Email"].widget.attrs.update({"placeholder" : "email", "class" : "account-input email-input"})
            self.fields["PW1"].widget.attrs.update({"placeholder" : "password", "class" : "account-input pw1-input"})
            self.fields["PW2"].widget.attrs.update({"placeholder" : "password check", "class" : "account-input pw2-input"})

class FindAccountForm(forms.Form):
    Email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(FindAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False    
            self.fields[field].widget.attrs.update({"class" : "account-input find-account-input", "placeholder" : "input your email"})








    
    

