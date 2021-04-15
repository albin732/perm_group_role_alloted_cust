from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DetailModel(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'admin'),
        ('sub_admin', 'sub_admin')
    )
    user = models.OneToOneField(
        User, related_name='detail', on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=30, choices=USER_TYPE_CHOICES, default='sub_admin')

    class Meta:
        db_table = "detail"

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(DetailModel, self).save(*args, **kwargs)
