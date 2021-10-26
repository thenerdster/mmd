from django import forms

from base.models import Clues, Characters, Solves

class SolveForm(forms.Form):
    name = forms.CharField(required=True)

    class Meta:
        model = Solves
        fields = (
            'whodonit',
            )