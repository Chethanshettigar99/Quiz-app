from django.contrib import admin
from django.contrib.auth.models import User  # Import the built-in User model
from quiz.models import Quiz

# Register Quiz model
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('question',)


