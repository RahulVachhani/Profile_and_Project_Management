from django.forms import ModelForm
from .models import Project, Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'   
        fields = ['title', 'image', 'discription','tags','source_link']

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs.update({'class': 'input', 'placeholder': f'add {name}'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        for name, field in self.fields.items():
            # print(name, field)
            field.widget.attrs.update({'class': 'input'})