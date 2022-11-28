from django import forms


class VoterLoginForm(forms.Form):
    matric = forms.CharField(max_length=15)
