from django import forms

class jobStatsForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'chosen-value', 'placeholder':'Search Category', 'autocomplete':'off'}))
    job_title = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Search Job Title / Keyword (optional)', 'autocomplete':'off'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Location (optional)', 'autocomplete':'off'}))

    junior = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'style':"all: revert", 'type':"checkbox"}))
    mid = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'style':"all: revert", 'type':"checkbox"}))
    senior = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'style':"all: revert", 'type':"checkbox"}))

    permanent = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'style':"all: revert", 'type':"checkbox"}))
    b2b  = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'style':"all: revert", 'type':"checkbox"}))
    mandate_contract = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'style':"all: revert", 'type':"checkbox"}))



class jobFindForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'chosen-value', 'placeholder':'Search Category', 'autocomplete':'off'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Location', 'autocomplete':'off'}))
    

