from django.db import models

class Memory(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField(default='2025-01-01')  # Provide a default value

    def __str__(self):
        return self.title
