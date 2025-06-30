from django.contrib import admin
from .models import DataUpload

@admin.register(DataUpload)
class DataUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('file',)
