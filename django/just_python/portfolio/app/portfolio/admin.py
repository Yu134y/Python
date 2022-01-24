from django.contrib import admin

from .models import Profile, Description, Skill, WorkDetail, Work


admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Skill)
admin.site.register(WorkDetail)
admin.site.register(Work)
