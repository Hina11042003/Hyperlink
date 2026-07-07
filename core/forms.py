from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(forms.Form):
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
    SKILLS = [
    ('py',  'Python'),
    ('js',  'JavaScript'),
    ('sql', 'SQL'),
]
    

    full_name = forms.CharField(error_messages={'required': 'Name is required'})
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    skills = forms.MultipleChoiceField(
    choices=SKILLS,
    widget=forms.CheckboxSelectMultiple
)
    agree = forms.BooleanField()
    dob        = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # resume = forms.FileField()
    # photo  = forms.ImageField()



    class Register(forms.Form):
      full_name = forms.CharField()
    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot contain numbers!")
        return name
    

    from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''