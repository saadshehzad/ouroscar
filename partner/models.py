from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"


class Partners(TimeStampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="partners")
    phone = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=40, null=True)

    class Meta:
        verbose_name = verbose_name_plural = "Partners"

    def __str__(self):
        return f"{self.user.first_name}"

