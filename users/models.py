from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_image_size(image):
    """
    (Optional) enforce a max file size (in bytes) so you can still
    prevent huge uploads without doing any image processing.
    """
    max_size = 2 * 1024 * 1024  # 2 MB
    if image.size > max_size:
        raise ValidationError("Image file too large ( > 2MB )")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profilepics/default.jpg',
        upload_to='profilepics',
        blank=True,
        validators=[validate_image_size],  # remove if you don’t need file‐size checks
    )
    status = models.CharField(max_length=30)
    about = models.TextField()

    def save(self, *args, **kwargs):
        # No resizing, just delegate to Django’s storage backend
        super().save(*args, **kwargs)
