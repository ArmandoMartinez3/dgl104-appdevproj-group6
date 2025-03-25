from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Administrator'),
        ('staff', 'Staff'),
        ('client', 'Client')
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='client')
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def is_admin(self):
        return self.user_type == 'admin' or self.is_superuser
    
    def is_staff_member(self):
        return self.user_type == 'staff'
    
    def is_client(self):
        return self.user_type == 'client'
