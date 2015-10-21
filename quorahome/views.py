from django.shortcuts import get_object_or_404, redirect, render

from .models import Question
# Create your views here.

def questions(request):
    context = {}
    return render(request, 'questions.html', context)
