from django.db import models

from django.contrib.auth import get_user_model


class Snack(models.Model):
    """
    create Snack Table in the database
    """
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'Our Snack'
        ver_name_plural = 'Our Snacks'