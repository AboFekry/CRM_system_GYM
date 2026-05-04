from django.contrib import admin
from .models import (
    Member, Trainer, MembershipPlan,
    Membership, GymClass, Booking
)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'active')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization')


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_months', 'price')


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'start_date', 'end_date', 'active')
    list_filter = ('active',)


@admin.register(GymClass)
class GymClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'schedule_time', 'max_capacity')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('member', 'gym_class', 'booked_at')


