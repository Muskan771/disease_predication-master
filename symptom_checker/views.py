from django.shortcuts import render

from .forms import SymptomForm
from .models import Disease

def check_symptoms(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data['symptoms']
            # Find diseases that match the selected symptoms
            diseases = Disease.objects.filter(symptoms__in=selected_symptoms).distinct()
            return render(request, 'results.html', {'diseases': diseases})
    else:
        form = SymptomForm()

    return render(request, 'symptom_checker.html', {'form': form})
# Create your views here.
