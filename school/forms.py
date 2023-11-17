from django import forms
from django.contrib.auth.models import User
from . import models


# for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        return password


# for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        return password


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['roll', 'mobile', 'fee', 'cl']
        widgets = {
            'roll': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter roll number'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter fee amount'}),
            'cl': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number should contain only digits")
        if len(mobile) < 10:
            raise forms.ValidationError("Mobile number should be at least 10 digits")
        return mobile

    def clean_roll(self):
        roll = self.cleaned_data.get('roll')
        if not roll.isalnum():
            raise forms.ValidationError("Roll number should contain only letters and numbers")
        return roll


# for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        return password


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.TeacherExtra
        fields = ['salary', 'mobile']
        widgets = {
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter salary'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number should contain only digits")
        if len(mobile) < 10:
            raise forms.ValidationError("Mobile number should be at least 10 digits")
        return mobile


# for Attendance related form
presence_choices = (("Present", "Present"), ("Absent", "Absent"))


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = ['roll', 'date', 'cl', 'present_status']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cl': forms.Select(attrs={'class': 'form-control'}),
            'present_status': forms.Select(attrs={'class': 'form-control'}, choices=[('Present', 'Present'), ('Absent', 'Absent')]),
        }


class AskDateForm(forms.Form):
    date = forms.DateField()


# for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = ['message', 'by']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notice message',
                'rows': 4
            }),
            'by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message should be at least 10 characters long")
        return message


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={"rows": 3, "cols": 30})
    )
