from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    RATING_CHOICES = [
        ('S', 'Safe'),
        ('Q', 'Questionable'),
        ('E', 'Explicit'),
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    tags = forms.CharField(max_length=2000)

    class Meta:
        model = Post
        fields = ['title', 'tags', 'rating', 'source', 'file']  # Assuming 'file' is the name of your FileField
