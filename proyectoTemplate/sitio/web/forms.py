# web/forms.py
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']  # Ajusta los campos aquí
 # Ajusta los campos según tu modelo
