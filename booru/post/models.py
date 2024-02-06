from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    RATING_CHOICES = [
        ('S', 'Safe'),
        ('Q', 'Questionable'),
        ('E', 'Explicit'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=2000)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='S')
    score = models.IntegerField(default=0, editable=False)
    source = models.CharField(max_length=255, blank=True, default='')
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return f"Post by {self.user.username} - {self.posted_date}"
