import uuid
from django.conf import settings
from django.db import models
from useraccount.models import User

# Create your models here.
class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    guests = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country_code = models.CharField(max_length=2)
    category = models.CharField(max_length=255)
    # favorites
    image = models.ImageField(upload_to='uploads/properties/', null=True, blank=True)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)
    # the 
    def image_url(self):
        # the following code is to avoid the error when the image is not set
        if self.image and hasattr(self.image, 'url'):
            return f'{settings.WEBSITE_URL}{self.image.url}'
        else:
            return None
