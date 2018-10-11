from django.db import models


# Create your models here.
# 问题
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    #打印出来更美观一些，加了，打印出来的结果就是中文，不加在后台出现的就是原对象
    def __unicode__(self):
        return self.question_text


# 选择
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
