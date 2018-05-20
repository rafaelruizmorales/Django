from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline): #admin.StackedInline
  model = Choice
  extra = 3


''' 1) Changing the order fields appear '''
# class QuestionAdmin(admin.ModelAdmin):
#   fields = ['pub_date', 'question_text']

''' 2) Using fieldsets '''
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,               {'fields': ['question_text']}),
      ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  
  list_filter = ['pub_date']
  search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)