""" Imports for the models and user """
from django.db import models
from django.contrib.auth.models import User
from shoppingapp.models import Macrame


class Review(models.Model):
    """ A model for the reviewing macrames """
    title = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    product_reviewed = models.ForeignKey(Macrame,related_name='product_reviewed', on_delete=models.CASCADE)
    user_reviewing = models.ForeignKey(User,related_name='user_reviewing', on_delete=models.CASCADE)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
