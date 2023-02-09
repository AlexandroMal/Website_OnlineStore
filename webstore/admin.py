from django.contrib import admin
from .models import telephones_Base, notebook_Base, desktop_Base, console_Base

admin.site.register(telephones_Base)
admin.site.register(notebook_Base)
admin.site.register(desktop_Base)
admin.site.register(console_Base)

