from django.contrib import admin

from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):  # admin.StackedInline takes too much space to display
    model = Choice
    extra = 3  # defines that by default, will provide enough fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
        # By default Django displays the str() of each object, but this makes it display individual fields.
        # list_display: a tuple of field names to display.
    list_filter = ['pub_date']  # allows to filter by different dates on admin page
    search_fields = ['question_text']  # adds search of question text
        # Limiting number of search fields to a reasonable number will make it easier for database to do the search.
    # Could also use list_per_page and date_hierarchy.

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) <-- inefficient way to do it; use inline instead.
