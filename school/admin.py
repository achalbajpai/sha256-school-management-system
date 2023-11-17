from django.contrib import admin
from .models import *

"""
Admin configuration for the school management system.
Register models to make them accessible in the Django admin interface.
"""

admin.site.register(TeacherExtra)
admin.site.register(StudentExtra)
admin.site.register(Notice)
admin.site.register(Attendance)
