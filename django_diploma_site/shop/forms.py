from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage, Order


class RegistrationForm(UserCreationForm):
    """Registration form with required Email field."""

    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким Email уже существует.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ContactForm(forms.ModelForm):
    """Feedback form with built-in Email validation."""

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'topic', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
            'topic': forms.TextInput(attrs={'placeholder': 'Тема сообщения'}),
            'message': forms.Textarea(attrs={'placeholder': 'Опишите вопрос', 'rows': 5}),
        }


class CheckoutForm(forms.ModelForm):
    """Checkout form for turning the session cart into a saved order."""

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'comment']
        labels = {
            'full_name': 'Имя и фамилия',
            'email': 'Email',
            'phone': 'Телефон',
            'address': 'Адрес или способ получения',
            'comment': 'Комментарий к заказу',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Иван Иванов'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+371 20000000'}),
            'address': forms.TextInput(attrs={'placeholder': 'Самовывоз / адрес доставки'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Дополнительная информация', 'rows': 4}),
        }
