from django.contrib import admin
from .models import Block, Apartment, Dues, Expense

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('block', 'number', 'owner', 'is_occupied')
    list_filter = ('block', 'is_occupied')
    search_fields = ('number', 'owner__username')

@admin.register(Dues)
class DuesAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'amount', 'due_date', 'is_paid', 'payment_date')
    list_filter = ('is_paid', 'due_date')
    search_fields = ('apartment__number', 'apartment__owner__username')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'category')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')
