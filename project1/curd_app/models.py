from django.db import models


class Employee(models.Model):
    DO_YOU_HAVE_ANY_LONG_TERM_INSURANCE = [("YES", "YES"), ("NO", "NO")]
    GENDER = [("Male", "Male"), ("FeMale", "FeMale")]
    full_name = models.CharField(max_length=20)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    emergency_contact_no = models.IntegerField()
    do_you_have_any_long_term_insurance = models.CharField(max_length=5, choices=DO_YOU_HAVE_ANY_LONG_TERM_INSURANCE)
    reference_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER)


