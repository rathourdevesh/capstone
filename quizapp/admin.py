from django.contrib import admin

# Register your models here.

from .models import TypingTest, User,Contest,Questions,Submissions

admin.site.register(User)
admin.site.register(Contest)
admin.site.register(Questions)
admin.site.register(Submissions)
admin.site.register(TypingTest)