from django.shortcuts import get_object_or_404, redirect, render

from .models import Question
from .forms import QuestionForm
# Create your views here.

def questions(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request, 'questions.html', context)

def home(request):
    form = QuestionForm()
    context = {
        "form": form
    }
    return render(request, 'quorahome.html', context)
