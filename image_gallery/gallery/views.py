from django.shortcuts import render,redirect,get_object_or_404
from .forms import ImageForm
from .models import Image,ImageComment

def images(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"template.html",{"obj":obj})
    else:
        form=ImageForm()
        img = Image.objects.all().order_by('-id')

        return render(request,"template.html",{"img":img,"form":form})

def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('/')  # Redirect to the index page after deletion
    return redirect('/')  # Handle GET requests by redirecting to the index page

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    print(request)
    return render(request, 'image_detail.html', {'image': image})

# IMAGE COMMENTS on Homepage
def add_Imagecomment(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comment_text = request.POST.get('comment_text', '')
    if comment_text:
        ImageComment.objects.create(post=image, text=comment_text)
    return redirect('/')

def delete_Imagecomment(request, image_id, comment_id):
    image = get_object_or_404(Image, pk=image_id)
    comment = get_object_or_404(ImageComment, pk=comment_id)
    comment.delete()
    # Check if the logged-in user is the author of the comment
    #if request.user == comment.user:
        #comment.delete()
    return redirect('/')
