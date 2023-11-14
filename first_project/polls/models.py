from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    #ADDED LATER BUT DO NOT HAVE TO MAKE MIGRATIONS FOR SPECIAL METHODS
    def __str__(self):
        #return self.question_text
        return str(self.id)
        #if you want to get the ID

class Choice(models.Model):
    #ADDED RELATIONSHIP
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #NEW CHANGE IN THE MODEL
    additional_text=models.TextField("Add Additional Information",default="no comments")
    #HAVE TO RUN 
    #python manage.py makemigrations
    #AND THEN
    #python manage.py migrate
    def __str__(self):
        return self.choice_text

class Task(models.Model):
    Title = models.CharField(max_length=100)
    Description=models.TextField("Description",default=" ")
    DueDate = models.DateTimeField("Due Date")
    def __str__(self):
        return self.Title
        
    #HAVE TO RUN 
    #python manage.py makemigrations
    #AND THEN
    #python manage.py migrate


class ArticleImage(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    file=models.FileField(upload_to='images')