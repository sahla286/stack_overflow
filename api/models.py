from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
        ans=Answers.objects.filter(question=self).values_list('id','answer','user__username','datetime')
        if ans:
            return list(ans)
            # formatted_answers = [(a[0], a[1], a[2], a[3].date()) for a in ans]
            # return formatted_answers
        else:
            return 'No Answer'

class Answers(models.Model):
    answer=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name='upvoters')
    
