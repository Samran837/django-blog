from PIL import Image
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        # Save the instance first
        super().save(*args, **kwargs)
        
        if self.image:  # Check if the profile picture exists
            img = Image.open(self.image)  # Open image from ImageField directly
            
            # Check if the image dimensions are too large
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)  # Save the resized image back
            
