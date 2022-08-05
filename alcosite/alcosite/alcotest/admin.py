from django.contrib import admin

from .models import *


def dublicate_ad(modeladmin, request, queryset):
    for ad in queryset:
        ad.pk = None
        ad.save()


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('num_question', 'question')


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer','weight_answer')
    actions = [dublicate_ad]


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers, AnswersAdmin)
