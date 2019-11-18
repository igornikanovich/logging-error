from django.db import models
from django.urls import reverse


class Application(models.Model):
    name = models.CharField(max_length=32)
    token = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app-detail', args=[self.pk])


class Error(models.Model):
    app = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='errors')
    date = models.DateTimeField()
    type = models.CharField(max_length=128)
    message = models.TextField()
    stacktrace = models.TextField()

    def __str__(self):
        return '{},{}'.format(self.type, self.date)
