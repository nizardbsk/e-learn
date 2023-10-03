from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class UpdateUserForm(ModelForm):
    class Meta:
        model=Profile
        fields=['bio','username','avatar']
class TutorialCreationForm(ModelForm):
    class Meta:
        model= Tutorial
        fields=['name','cover','description','price']
class VideoForm(ModelForm):
    class Meta:
        model= Video
        fields=['title','video','description']
