from django import forms
from .models import to_do_list


class to_do_Form(forms.ModelForm):
    class Meta:
        model = to_do_list
        fields = "__all__"