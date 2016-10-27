from polls.models import Poll
from polls.models import Choice
from django.contrib import admin
from polls.models import Question


class PollAdmin(admin.ModelAdmin):
    """
    Poll admin model
    """

    list_display = ('name', 'user')
    list_filter = ('user',)

admin.site.register(Poll, PollAdmin)


class ChoiceAdmin(admin.TabularInline):
    """
    Choice admin model
    """

    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin model
    """

    list_display = ('question_text', 'total_voter', 'pub_date')
    list_filter = ('question_text', 'pub_date')

    inlines = [
        ChoiceAdmin,
    ]

admin.site.register(Question, QuestionAdmin)