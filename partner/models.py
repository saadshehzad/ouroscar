from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Partner(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
class PartnerAddress(TimeStampMixin):
    partner = models.OneToOneField(Partner, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)