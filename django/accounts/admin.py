from django.contrib import admin
from unfold.admin import ModelAdmin
from accounts.models import Account


class AccountAdmin(ModelAdmin):
    list_display = ('username', 'get_account_name', 'email', 'is_active',)

    def get_account_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    get_account_name.admin_order_field  = 'account' 
    get_account_name.short_description = 'Name'

admin.site.register(Account, AccountAdmin)
