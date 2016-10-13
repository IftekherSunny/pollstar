from polls.models import Poll
from polls.models import Choice
from django.contrib import admin
from polls.models import Question


# Poll admin model
class PollAdmin(admin.ModelAdmin):
    pass

admin.site.register(Poll, PollAdmin)


# Question admin model
class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)


# Choice admin model
class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Choice, ChoiceAdmin)
