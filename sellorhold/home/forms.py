from django import forms

class UserInput(forms.Form):
    company_name = forms.CharField(
        max_length=120,
        required = True,
        widget = forms.TextInput(attrs={"id": "company_name", "placeholder": "Company name", "class": "form-control"})
    )
    
    vest_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"type": "date", "id": "vest_date", "class": "form-control"})
    )