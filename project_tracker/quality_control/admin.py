from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.action(description='Изменить статус на \"в работе\"')
def set_In_progress(self, request, queryset):
    count = queryset.update(status=BugReport.In_progress)
    self.message_user(request, f"Изменено {count} записи(ей).")

@admin.action(description='Изменить статус на \"завершена\"')
def set_Completed(self, request, queryset):
    count = queryset.update(status=BugReport.Completed)
    self.message_user(request, f"Изменено {count} записи(ей).")

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    fieldsets = [('Main options', {"fields": ["title", "project", "task"]}),
                 ('Advanced options', {"fields": ['status', 'priority', 'description']})]

    actions = [set_In_progress, set_Completed]

@admin.register(FeatureRequest)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'description')
    fieldsets = [('Main options', {"fields": ["title", "project", "task"]}),
                 ('Advanced options', {"fields": ['status', 'priority', 'description']})]