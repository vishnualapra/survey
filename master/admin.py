from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Files)
admin.site.register(models.Participants)
admin.site.register(models.UserFiles)
admin.site.register(models.SurveyResult)

