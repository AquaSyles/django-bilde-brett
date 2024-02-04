from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserOptions(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # Tag Blacklist
    blacklisted_tags = models.TextField(blank=True, null=True, help_text="Comma-separated list of blacklisted tags")

    # Blacklist Rating
    BLACKLIST_RATING_CHOICES = [
        ('safe', 'Safe'),
        ('questionable', 'Questionable'),
        ('explicit', 'Explicit'),
        ('s', 'Safe'),
        ('q', 'Questionable'),
        ('e', 'Explicit'),
    ]
    blacklisted_rating = models.CharField(max_length=12, choices=BLACKLIST_RATING_CHOICES, blank=True, null=True)

    # Blacklist Users
    blacklisted_users = models.ManyToManyField(User, related_name='blacklisted_users', blank=True)

    # Comment Threshold
    comment_threshold = models.IntegerField(default=0, help_text="Ignore comments with a score below this threshold")

    # Post Threshold
    post_threshold = models.IntegerField(default=0, help_text="Ignore posts with a score below this threshold")

    # NSFW images
    show_nsfw_images = models.BooleanField(default=True, help_text="Show or hide NSFW images")

    # Theme (example: dark, light)
    theme = models.CharField(max_length=20, default='light', help_text="User's preferred theme")

    def __str__(self):
        return f"Options for {self.user.username}"

@receiver(post_save, sender=User)
def create_user_options(sender, instance, created, **kwargs):
    if created:
        UserOptions.objects.create(user=instance)