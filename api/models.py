from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    title=models.CharField(max_length=100)
    question=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.question
    
    @property
    def qus_ans(self):
        ans=self.answers_set.all()
        return ans
    

class Answers(models.Model):
    answer=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name='upvoters')
    
    def __str__(self) :
        return self.answer
    
    @property
    def upvote_count(self):
        count_upvote=self.upvote.all()
        if count_upvote:
            return count_upvote.count()
        else:
            return 0
    
    