from django import forms
from .models import acc

class userform(forms.ModelForm):
    class Meta:
        model=acc
        fields=['username','accountnumber','phone']

class loginf(forms.Form):
    data=forms.CharField(max_length=10)

class transfer(forms.Form):
    sender=forms.IntegerField()
    reciver=forms.IntegerField()
    amount=forms.IntegerField()