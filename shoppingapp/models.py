""" Imports for modules ad models """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """ A category of the products with a user-friendly name """
    class Meta:
        """ Helper class for plural names """
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ A method to show name of the category """
        return self.name

    def get_friendly_name(self):
        """ A method to show user-friendly name of the categories """
        return self.friendly_name


class Macrame(models.Model):
    """ A model of macrame attributes """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return self.name

    def number_of_likes(self):
        """ A helper method to count likes """
        return self.likes.count()


class Review(models.Model):
    """ A model for the reviewing products """
    title = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    product_reviewed = models.ForeignKey(Macrame, related_name='reviews',
                                         on_delete=models.CASCADE)
    user_reviewing = models.ForeignKey(User, related_name='reviews',
                                         on_delete=models.CASCADE)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        """ Order of reviews """
        ordering = ['created_at']

    def __str__(self):
        """ A helper method for seeing the title """
        return self.title
