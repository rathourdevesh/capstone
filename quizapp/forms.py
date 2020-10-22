from django import forms
from .models import Questions

class testPageForm(forms.ModelForm):
    
    class Meta:
        model = Questions
        Choice = (('1','One'),('2','Two'),('3','Three'),('4','Four'),)
        exclude = (),
        fileds = ['question','ansChoice']