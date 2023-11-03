from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE,
                               null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title
