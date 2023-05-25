from django import forms

class Parameters(forms.Form):
    age = forms.IntegerField(max_value=120,min_value=1 , widget=forms.NumberInput(attrs={'id':'a1' , 'type':'text','class':'validate'}) , error_messages={'invalid':'Please enter a number'})
    sex= forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a2' , 'type':'text','class':'validate'}))
    cp = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a3' , 'type':'text','class':'validate'}))
    trestbps = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a4' , 'type':'text','class':'validate'}))
    chol = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a5' , 'type':'text','class':'validate'}))
    fbs = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a6' , 'type':'text','class':'validate'}))
    restcg = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a7' , 'type':'text','class':'validate'}))
    thalach = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a8' , 'type':'text','class':'validate'}))
    exang = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a9' , 'type':'text','class':'validate'}))
    oldpeak = forms.FloatField(widget=forms.NumberInput(attrs={'id':'a10' , 'type':'text','class':'validate'}))
    slope = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a11' , 'type':'text','class':'validate'}))
    ca = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a12' , 'type':'text','class':'validate'}))
    thal= forms.IntegerField(widget=forms.NumberInput(attrs={'id':'a13' , 'type':'text','class':'validate'}))
    
