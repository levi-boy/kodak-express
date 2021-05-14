from django.contrib import admin

from .models import OrderModel, MailModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(MailModel)
class MailAdmin(admin.ModelAdmin):
    pass
