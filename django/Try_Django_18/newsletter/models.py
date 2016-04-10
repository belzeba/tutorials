from django.db import models


# Create your models here.
# Model for Sign up
class SignUp(models.Model):
    email = models.EmailField()
    # Maximum of 120 characters, can be blank in form and null in database
    full_name = models.CharField(max_length=120, blank=True, null=True)
    # Add 'now' time on insert but not on update
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Add 'now' time on update but not on insert
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # What to return when we print this object
    def __str__(self):  # Python 2.7.* is __unicode__
        return self.email
