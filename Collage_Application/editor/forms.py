from django import forms

class VideoEditForm(forms.Form):
    video = forms.FileField()
    start_time = forms.CharField(help_text="Format: HH:MM:SS")
    end_time = forms.CharField(help_text="Format: HH:MM:SS")
    split_audio = forms.BooleanField(required=False)

# app/forms.py

 

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name'
        })
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address'
        })
    )
    
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your message here',
            'width':'200px'

        })
    )
    
    attachment = forms.FileField(
        label='Attach a file',
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'placeholder': 'Upload a file'
        })
    )

