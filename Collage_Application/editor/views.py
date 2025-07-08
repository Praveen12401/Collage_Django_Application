from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
import os
import subprocess
from django.http import FileResponse
from .forms import VideoEditForm
from django.conf import settings
import uuid

def edit_video(request):
    if request.method == 'POST':
        form = VideoEditForm(request.POST, request.FILES)
        if form.is_valid():
            video = request.FILES['video']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            split_audio = form.cleaned_data['split_audio']

            input_path = os.path.join(settings.MEDIA_ROOT, str(uuid.uuid4()) + video.name)
            output_video = input_path.replace('.mp4', '_cut.mp4')
            output_audio = input_path.replace('.mp4', '_audio.mp3')

            # Save uploaded video
            with open(input_path, 'wb+') as f:
                for chunk in video.chunks():
                    f.write(chunk)

            # FFmpeg: Cut video
            cmd_video = [
                'ffmpeg', '-i', input_path, '-ss', start, '-to', end,
                '-c', 'copy', output_video
            ]
            subprocess.run(cmd_video)

            if split_audio:
                # FFmpeg: Extract audio
                cmd_audio = [
                    'ffmpeg', '-i', output_video, '-q:a', '0', '-map', 'a', output_audio
                ]
                subprocess.run(cmd_audio)

                return FileResponse(open(output_audio, 'rb'), as_attachment=True)

            return FileResponse(open(output_video, 'rb'), as_attachment=True)
    else:
        form = VideoEditForm()

    return render(request, 'editor/edit.html', {'form': form})
    
