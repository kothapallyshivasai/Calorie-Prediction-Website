from django import forms

class HealthForm(forms.Form):
    age = forms.FloatField(label='Age', required=True)
    height = forms.FloatField(label='Height (cm)', required=True)
    weight = forms.FloatField(label='Weight (kg)', required=True)
    duration = forms.FloatField(label='Duration (minutes)', required=True)
    heart_rate = forms.FloatField(label='Heart Rate (bpm)', required=True)
    body_temp = forms.FloatField(label='Body Temperature (°C)', required=True)
    gender_male = forms.ChoiceField(choices=[(1, 'Male'), (0, 'Female')], label='Gender', required=True)
