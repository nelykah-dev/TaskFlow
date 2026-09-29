from django.shortcuts import render , redirect
from.models import Taches
from .forms import TachesForm


def liste_taches(request):
    taches = Taches.objects.all()
    return render(request, 'Taskflow/list.html',{'taches': taches})

def creer_tache(request):
    if request.method == 'POST':
        form = TachesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_taches')
    else:
        form = TachesForm()
    return render(request, 'Taskflow/list.html', {'form': form})