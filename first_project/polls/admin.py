from django.contrib import admin

# Register your models here.



#NEWLY ADDED CODE FOR SUPER USER TUTORIAL
from .models import Question,Choice,Task

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Task)

#CRUCIAL LERARNING MOMENT HAVE TO REGISTER TO ADMIN 
