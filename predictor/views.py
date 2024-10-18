from django.shortcuts import render
import pickle
import numpy as np
from .forms import HealthForm

with open("./model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

def home(request):
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            duration = form.cleaned_data['duration']
            heart_rate = form.cleaned_data['heart_rate']
            body_temp = form.cleaned_data['body_temp']
            gender_male = int(form.cleaned_data['gender_male'])

            bmi = weight / ((height / 100) ** 2)

            X_array = np.array([[age, bmi, duration, heart_rate, body_temp, gender_male]]).reshape(1, -1)
            y_pred = loaded_model.predict(X_array)
            
            return render(request, 'predictor/result.html', {'prediction': round(y_pred[0], 2)})

    else:
        form = HealthForm()
    
    return render(request, 'predictor/index.html', {'form': form})
