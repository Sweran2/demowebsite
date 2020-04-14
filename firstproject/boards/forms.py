from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':5, 'placeholder':'what is the message'
    }), max_length='5000', help_text='maxmimum charchters 150 letter')
    class Meta:
        model = Topic
        fields = ['subject','message']

class PostForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows':5, 'placeholder':'Your reply .. '
    }), max_length='5000', help_text='maxmimum charchters 150 letter')

    class Meta:
        model = Post
        fields = ['message']
