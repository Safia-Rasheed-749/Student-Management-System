from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course', 'address', 'profile_picture']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border border-[#286e6f] rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-[#286e6f] text-gray-800'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-[#286e6f] rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-[#286e6f] text-gray-800'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'border border-[#286e6f] rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-[#286e6f] text-gray-800'
            }),
            'course': forms.TextInput(attrs={
                'class': 'border border-[#286e6f] rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-[#286e6f] text-gray-800'
            }),
            'address': forms.Textarea(attrs={
                'class': 'border border-[#286e6f] rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-[#286e6f] text-gray-800',
                'rows': 3
            }),
        }


