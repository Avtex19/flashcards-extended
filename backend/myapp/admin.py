# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_date',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_date',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Deck)
admin.site.register(Flashcard)
admin.site.register(Category)
admin.site.register(Hint)

