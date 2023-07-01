from django.shortcuts import render, redirect
from .models import *

def all_leave(request):
    leave = LeaveForm.objects.filter(check_in_status = False)
    print(leave)
    context = {'leave': leave}
    return render(request, 'all_leave.html', context)

 

def approve_view(request, id):
    leave = LeaveForm.objects.get(id = id)
    leave.status = True
    leave.check_in_status = True
    leave.save()
    return redirect('all_leave')


def reject_view(request, id):
    leave = LeaveForm.objects.get(id = id)
    leave.status = False
    leave.check_in_status = True
    leave.save()
    return redirect('all_leave')