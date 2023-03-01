from django.db import models
from partner.models import TimeStampMixin, User


class CustomUser(TimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)