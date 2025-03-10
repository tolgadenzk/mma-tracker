from django.shortcuts import render, get_object_or_404, redirect
from .models import TrainingSession
from .forms import TrainingForm
from django.shortcuts import render, redirect
from .forms import TrainingForm
from collections import Counter
from .models import TrainingSession


def add_training(request):
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm()

    return render(request, 'training/add_training.html', {'form': form})





def edit_training(request, training_id):
    training = get_object_or_404(TrainingSession, pk=training_id)


    
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingForm(instance=training)
    
    return render(request, 'training/edit_training.html', {'form': form})

def delete_training(request, training_id):
    training = get_object_or_404(TrainingSession, pk=training_id)
    training.delete()
    return redirect('/')

def training_list(request):
    trainings = TrainingSession.objects.all().order_by('-date')

    # Toplam antrenman sayısı
    total_trainings = trainings.count()

    # Toplam antrenman süresi
    total_duration = sum(training.duration for training in trainings)

    # En çok yapılan antrenman türünü bul
    if trainings:
        training_types = [training.training_type for training in trainings]
        most_common_training = Counter(training_types).most_common(1)[0][0]  # En çok tekrar eden antrenman türü
    else:
        most_common_training = "Henüz antrenman eklenmedi"

    context = {
        'trainings': trainings,
        'total_trainings': total_trainings,
        'total_duration': total_duration,
        'most_common_training': most_common_training
    }

    return render(request, 'training/training_list.html', context)