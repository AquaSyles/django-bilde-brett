from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.db import models

class UserOptions(models.Model):
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


class CustomUser(AbstractUser):
    # One-to-One relationship with UserOptions
    user_options = models.OneToOneField(UserOptions, on_delete=models.CASCADE, null=True, blank=True, related_name='user_options')

    # Provide unique related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)