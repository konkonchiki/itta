from cProfile import label
from dataclasses import fields
from django import forms
from .models import Topics , Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model           = Topics
        fields          = ['topic_title']
        labels          = {'topic_title':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model           = Entry
        fields          = ['detailTopic']
        labels          = {'detailTopic':''}
        widgets         = {'detailTopic':forms.Textarea(attrs={'cols':120})}
        
        