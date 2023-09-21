from django.contrib import admin
from .models import Institute,ProjectInstituteStudent,AnyStudent,Projects

admin.site.register(Institute)
admin.site.register(ProjectInstituteStudent)
admin.site.register(AnyStudent)
admin.site.register(Projects)