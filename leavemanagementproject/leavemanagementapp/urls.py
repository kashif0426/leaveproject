from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all_leave', all_leave, name = 'all_leave'),
    path('approve_view/<int:id>', approve_view, name = 'approve_view'),
    path('reject_view/<int:id>', reject_view, name = 'reject_view')
]
