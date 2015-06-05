import datetime  # Python's standard datetime module

from django.db import models
from django.utils import timezone  # Django's time-zone-related utilities

"""With this info, django can:
1) Create a database schema (CREATE TABLE statements) for this app.
2) Create a Python database-access API for accessing Question and Choice objects."""

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # max_length is req'd for CharField
    pub_date = models.DateTimeField('date published')  # includes human-readable name

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'  # allows us to sort by was_published_recently
    was_published_recently.boolean = True  # says it's a boolean, so shows up as a check/'x' on admin page
    was_published_recently.short_description = 'Published recently?'  # sets title of column on admin page

class Choice(models.Model):
    question = models.ForeignKey(Question)  # says that each Choice is related to a single Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # default number of votes = 0

    def __unicode__(self):
        return self.choice_text