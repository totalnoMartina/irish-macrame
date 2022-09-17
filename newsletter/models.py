from django.db import models


class NewsletterUser(models.Model):
    """ A model for the people to subscribe for newsletter """
    email_user = models.EmailField(blank=True)