from django import forms

class InputForm(forms.Form):
    user_input = forms.IntegerField(label='Por favor escriba la suma de las alturas', min_value=0)