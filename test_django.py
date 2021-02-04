from django.db import connection
from .models import User

def my_view(self):
    # this is bad
    User.objects.raw("SELECT * FROM myapp_person WHERE last_name = %s" % lname)
    # this bypasses Django's SQL injection protection, but harder to detect
    User.objects.raw("SELECT * FROM myapp_person WHERE last_name = '%s'", [lname])
