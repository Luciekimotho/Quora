from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        fields = ['question']
        model = Question

class AnswerForm(forms.ModelForm):
    class Meta:
        fields = ['answer']
        model = Answer

