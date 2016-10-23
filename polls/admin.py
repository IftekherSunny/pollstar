from polls.models import Poll
from polls.models import Choice
from django.contrib import admin
from polls.models import Question


# Poll admin model
class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('user',)

admin.site.register(Poll, PollAdmin)


# Choice admin model
class ChoiceAdmin(admin.TabularInline):
    model = Choice
    extra = 1


# Question admin model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'total_voter', 'pub_date')
    list_filter = ('question_text', 'pub_date')

    inlines = [
        ChoiceAdmin,
    ]

admin.site.register(Question, QuestionAdmin)
