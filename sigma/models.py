from django.db import models

class Quote(models.Model):
    author = models.CharField(max_length=150)
    author_quote = models.CharField(max_length=500)

    def __str__(self):
        return self.author
