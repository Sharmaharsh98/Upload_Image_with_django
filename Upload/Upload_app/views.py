
from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
def image_upload_view(request):
    form = ImageForm()
    template_name = 'Upload_app/index.html'

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, template_name, {'form': form, 'img_obj': img_obj})

    return render(request, template_name, {'form': form})


