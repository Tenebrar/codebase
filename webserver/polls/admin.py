from django.contrib import admin

from webserver.polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['publication_time'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'publication_time', 'was_published_recently')
    list_filter = ['publication_time']
    search_fields = ['text']


admin.site.register(Question, QuestionAdmin)
