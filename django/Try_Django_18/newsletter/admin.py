from django.contrib import admin
from .models import SignUp  # Own model
from .forms import SignUpForm  # Custom form


# Register your models here.
# Own admin class
class SignUpAdmin(admin.ModelAdmin):
    # What data to show in admin console
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
    """class Meta:
        model = SignUp"""


# Register our model for Admin site with newly created admin class
admin.site.register(SignUp, SignUpAdmin)
