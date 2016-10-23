from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    total_voter = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    class Meta:
        pass


class Choice(models.Model):
    ''' Choice model for the question model '''

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)

    total_vote = models.IntegerField(default=0)

    def getTotalVoteInPercentage(self):
        ''' Get total vote in percentage '''
        if (self.total_vote != 0) and (self.question.total_voter != 0):
           return (self.total_vote / self.question.total_voter) * 100
        else:
            return 0

    def __str__(self):
        return self.choice_text

    class Meta:
        ''' meta '''
        pass