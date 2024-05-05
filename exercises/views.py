# gym_tracker/views.py
from django.contrib.auth.decorators import login_required  
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Exercise
from .forms import ExerciseForm
from django.http import JsonResponse


from django.shortcuts import render
from django.http import JsonResponse
from .forms import ExerciseForm
from .models import Exercise

def exercise_view(request):
    """Render the exercise form initially and handle form submission."""
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            # Fetch all exercises after adding the new one
            exercises = Exercise.objects.all().values()
            return JsonResponse({'exercises': list(exercises)})
    else:
        form = ExerciseForm()
    
    context = {'form': form}
    return render(request, 'exercises.html', context)



@login_required
def all_exercises_view(request):
    """Retrieve all exercise data for logged-in user."""

    exercises = Exercise.objects.filter(user=request.user)  # Filter for current user
    data = [
        {
            'id': exercise.id,
            'date_time': exercise.date_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': exercise.duration,
            'exercise_name': exercise.exercise_name,
            'sets': exercise.sets,
            'reps': exercise.reps
        }
        for exercise in exercises
    ]
    return JsonResponse({'data': data})