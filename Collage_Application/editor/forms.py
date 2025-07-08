from django import forms

class VideoEditForm(forms.Form):
    video = forms.FileField()
    start_time = forms.CharField(help_text="Format: HH:MM:SS")
    end_time = forms.CharField(help_text="Format: HH:MM:SS")
    split_audio = forms.BooleanField(required=False)
