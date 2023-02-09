from django.contrib import admin

from .models import PartnerAddress, Partners


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("id","created_at", "updated_at", "user")
    list_filter = ("created_at", "updated_at", "user")
    date_hierarchy = "created_at"


@admin.register(PartnerAddress)
class PartnerAddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "partner",
        "city",
        "country",
    )
    list_filter = ("created_at", "updated_at", "partner")
    date_hierarchy = "created_at"
