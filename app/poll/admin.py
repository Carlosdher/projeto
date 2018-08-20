from django.contrib import admin
from .models import UUIDUser, Propose, Comment

admin.site.register(Propose)
admin.site.register(UUIDUser)
admin.site.register(Comment)
