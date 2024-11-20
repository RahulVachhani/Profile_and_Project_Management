from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Message
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        

            # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        for name, field in self.fields.items():
     
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','bio','short_intro','profile_img','social_github','social_linkedIn','social_youtube']


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        

            # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        for name, field in self.fields.items():
     
            field.widget.attrs.update({'class': 'input'})

    
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']


    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        

            # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        for name, field in self.fields.items():
     
            field.widget.attrs.update({'class': 'input'})

        
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        

            # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'add title'})

        for name, field in self.fields.items():
     
            field.widget.attrs.update({'class': 'input'})