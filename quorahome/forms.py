from django import forms
from .models import Question

class QuestionForm(forms.modelForm):
    class Meta:
        fields = ['question']
        model = Questions
