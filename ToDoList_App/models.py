from django.db import models
from datetime import datetime
from django.utils.text import slugify
# Create your models here.


class Tasks(models.Model):
    email = models.CharField(max_length=50, default='username')
    # slug = models.SlugField(unique=True, default='slug')
    start_date = models.CharField(max_length=50, default='start date and time')
    end_date = models.CharField(max_length=50, default=' end date and time')
    type = models.CharField(max_length=50, default=' Personal')
    is_archive = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_InProgress = models.BooleanField(default=True)
    Task = models.TextField()

    def save(self, *args, **kwargs):
        now = datetime.now()
        today = now.date()
        self.start_date = str(today)
        # self.slug = slugify(self.email)
        super(Tasks, self).save(*args, **kwargs)


