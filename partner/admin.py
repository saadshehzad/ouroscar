from django.contrib import admin

from .models import Partners, CustomUser

admin.site.register(CustomUser)

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("id","created_at", "updated_at", "user", "address")
    list_filter = ("created_at", "updated_at", "user")
    date_hierarchy = "created_at"