from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm, AnswerForm
# Create your views here.

def questions(request):
    questions = Question.objects.all()
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answers = form.save(commit=False)
        answers.questions = questions
        answers.save()
        return redirect(request.path)
    context = {'questions':questions,
               'form': form
              }
    return render(request, 'questions.html', context)

def home(request):
    form = QuestionForm(request.POST or None)
    print (request.POST)
    context = {
        "form": form
    }
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
    return render(request, 'quorahome.html', context)

