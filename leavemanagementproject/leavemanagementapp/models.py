from django.db import models
from django.contrib.auth.models import User

class LeaveForm(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    leave_pupose = models.CharField(max_length = 500, blank = True, null = True)
    status = models.BooleanField(default = False)
    check_in_status = models.BooleanField(default = False)
                                             

    def __str__(self):
        return self.leave_pupose