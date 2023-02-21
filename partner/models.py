from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Partners(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=40, null=True)

    class Meta:
        verbose_name = verbose_name_plural = "Partners"

    def __str__(self):
        return f"{self.user.first_name}"


class CustomUser(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)