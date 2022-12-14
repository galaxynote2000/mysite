from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['question_texts']}),
    ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
