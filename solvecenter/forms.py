from django.core.exceptions import ValidationError
from . models import Issue, Resolution
from django import forms

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields= ['hardware','software','reported_issue','issue_pic']
        labels = {'hardware': 'Select Hardware to assign issue:','software':'Select Software to assing issue:','reported_issue':'Enter issue:','issue_pic': 'Upload PIcture:'}
    
    def clean(self):
        cleaned_data = super().clean()

        hard = cleaned_data.get('hardware')
        soft = cleaned_data.get('software')
        
        if hard and soft:
            raise ValidationError("Please make only one selection.")
        if not hard and not soft:
            raise ValidationError("Please make at least one selection.")
        return cleaned_data

class ResolutionForm(forms.ModelForm):
    class Meta:
        model = Resolution
        fields=['reported_resolution', 'resolution_pic']
        labels = {'reported_resolution': 'Enter resolution'}
