from .models import User
from django import forms
from django.forms import ValidationError
from .models import User



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
        self.fields["UserName"].widget.attrs.update({"class" : "account-input login-username","placeholder" : "username"})
        self.fields["PW"].widget.attrs.update({"class" : "account-input login-password","placeholder" : "password"})

    def clean(self):
            data = self.cleaned_data
            if(not User.objects.filter(UserName = data["UserName"], PW = data["PW"]).exists()):
                raise ValidationError("it's not assinged account")

            return self.cleaned_data




                

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

    def clean_UserName(self):
        username = self.cleaned_data["UserName"]

        if len(username) < 2 or len(username) > 15:
            raise ValidationError("username must be longer than 2character and shorter than 15 character")
        if User.objects.filter(UserName= username).exists():
            raise ValidationError("this name already using by someone")
        return username

    def clean(self):
        super().clean()
        pw1 = self.cleaned_data["PW1"]
        pw2 = self.cleaned_data["PW2"]

        if pw1 != pw2:
            raise ValidationError("password is not correct")
        if len(pw1) > 30 or len(pw1) < 10:
            raise ValidationError("password must be longer than 10 character and shorter than 30 character")

    def clean_Email(self):
        email = self.cleaned_data["Email"]
        if User.objects.filter(Email = email).exists():
            raise ValidationError("this Email already has account")
        return email
    
    def save(self, ip):
        data = self.cleaned_data
        newUser = User(UserName = data["UserName"], Email = data["Email"], PW = data["PW1"], UserIP = ip)
        newUser.save()

    

        
class FindAccountForm(forms.Form):
    Email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(FindAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False    
            self.fields[field].widget.attrs.update({"class" : "account-input find-account-input", "placeholder" : "input your email"})








    
    

