from django.db import models

class to_do_list(models.Model):
    Sr_No = models.IntegerField()
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    date = models.DateTimeField()

    class Meta:
        db_table = "employee"
