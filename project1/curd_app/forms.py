from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(),
            "blood_group": forms.TextInput(attrs={"class": "form-control"}),
            "emergency_contact_no": forms.NumberInput(),
            "do_you_have_any_long_term_insurance":  forms.Select(attrs={"class": "form-control"}),
            "reference_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"})

        }
