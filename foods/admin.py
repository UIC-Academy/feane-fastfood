from django.contrib import admin

from foods import models


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "is_active")
    list_display_links = ("id", "name")
    list_editable = ("is_active",)
    list_filter = ("category",)
    search_fields = ("name", "category__name")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message", "stars")
    list_display_links = ("id", "user")


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "phone_number", "email", "num_of_people", "datetime", "is_request_verified", "is_they_actually_come")
    list_display_links = ("id", "user_name")