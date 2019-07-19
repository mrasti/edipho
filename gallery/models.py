from django.db import models

class Photo(models.Model):
    title = models.CharField(default='', max_length = 300, blank=True, null=True)
    image = models.ImageField(blank = False, null = False)
    location = models.CharField(default='', max_length = 300, blank=True, null=True)
    time_uploaded = models.DateTimeField(auto_now_add = True, auto_now = False)
    filter = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.title

class Meta:
    ordering = ["time_uploaded"]

