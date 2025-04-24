from django.db import models

# Model for storing Newsletter subscribers
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Model for Instagram feed (if you plan to store Instagram posts dynamically)
class InstagramFeed(models.Model):
    image = models.ImageField(upload_to='instagram_images/')
    link = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instagram post {self.id}"
