from django.db import models


# Create your models her
class movie_list(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name
