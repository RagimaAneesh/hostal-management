from django.contrib import admin


from newapp import models

admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Parent)
admin.site.register(models.Food)
admin.site.register(models.Notification)
admin.site.register(models.Studentcomplaint)
admin.site.register(models.Feedback)
