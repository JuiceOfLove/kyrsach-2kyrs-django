from django.contrib import admin
from .models import User, News, Sale
from simple_history.admin import SimpleHistoryAdmin

@admin.register(User)
class users(SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(News)
class news(SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Sale)
class sales(SimpleHistoryAdmin):
    class Meta:
        proxy = True