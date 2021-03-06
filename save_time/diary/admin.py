from django.contrib import admin
from .models import Day, Challenge, Task, Frog, Steak, Joy, Memory

# Register your models here.
# admin.site.register(Day)
class TaskInstanceInline(admin.TabularInline):
    model = Task


class ChallengeInstanceInline(admin.TabularInline):
    model = Challenge




# Representation Frog model in Day instance with ManyToMany relationship
# class FrogInstanceInline(admin.TabularInline):
#     model = Frog.day.through
#
#
# class FrogAdmin(admin.ModelAdmin):
#     inlines = [FrogInstanceInline]


class DayAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [TaskInstanceInline, ChallengeInstanceInline]


admin.site.register(Day, DayAdmin)

# admin.site.register(Challenge)
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'day')


@admin.register(Frog)
class FrogAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'day')

# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'task_type', 'day')
    fieldsets = (
        ('Task menu', {
            'fields': ('name', 'task_type')
        }),
        ('Other info', {
            'fields': ('user', 'day')
        }),
    )
admin.site.register(Steak)
admin.site.register(Joy)
admin.site.register(Memory)
