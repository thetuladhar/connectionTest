from django.db import models
from django.db.models import ForeignKey

# Create your models here.
class Image(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/uploads")
    description=models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title#,self.description
class ImageComment(models.Model):
    post = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='comments')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)