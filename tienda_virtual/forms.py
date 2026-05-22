from django import forms
#from django.contrib.auth.models import User
from users.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username','placeholder': 'Nombre de usuario' }))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email','placeholder': 'ejemplo.dominio@dominio.com' }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password','placeholder': 'Contraseña' }))
    
    password2 = forms.CharField(required=True, label = 'Confirmar contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2','placeholder': 'Repetir contraseña' }))
    


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya existe')

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo electrónico ya está en uso')

        return email
    
    def clean(self): 
        cleaned__data = super().clean()

        if cleaned__data.get('password2') != cleaned__data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')

        return cleaned__data
    

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
    
    