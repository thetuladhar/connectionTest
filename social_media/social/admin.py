from django.contrib import admin

# Register your models here.

#NEWLY ADDED CODE FOR SUPER USER TUTORIAL
from .models import Post,Comment
from .models import Image,ImageComment
#from .models import UserProfile
#from .models import Like

admin.site.register(Post)
admin.site.register(Comment)

admin.site.register(Image)
admin.site.register(ImageComment)

#admin.site.register(UserProfile)


#CRUCIAL LERARNING MOMENT HAVE TO REGISTER TO ADMIN 