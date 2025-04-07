from django.db import models

class Comment(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    author = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField()
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.author} - {self.id}"