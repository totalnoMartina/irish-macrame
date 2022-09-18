""" Importof django models """
from django.db import models


class NewsletterUser(models.Model):
    """ A model for the people to subscribe for newsletter """
    email_user = models.EmailField(blank=True)

    def __str__(self):
        """ A method to see the email addresses """
        return self.email_user
