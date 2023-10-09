from django.db import models
from django.contrib.auth.models import User 
#from quizApp.models import BaseModel
# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Topic(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Question(BaseModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    explanation = models.TextField(blank=True, null=True)
    correct_option = models.ForeignKey('Option', on_delete=models.CASCADE, related_name='correct_for_question', null=True, blank=True)
    options = models.ManyToManyField('Option', related_name='question_options', blank=True, null=True)
    
    def __str__(self):
        return self.text
    
class Option(models.Model):
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + "----> "+ self.question.text +"---->"+ self.selected_option.text

    @property
    def is_correct(self):
        return self.selected_option == self.question.correct_option        
     
        
# Option.objects.bulk_create([Option(text="500"),Option(text="300",is_correct=True),Option(text="100"),Option(text="250")])