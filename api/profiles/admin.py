from django.contrib import admin
from .models import Profile, Link


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_account', 'title', 'is_active',)

    def get_account(self, obj):
        return obj.account.first_name + ' ' + obj.account.last_name

    get_account.admin_order_field  = 'account' 
    get_account.short_description = 'Account Name'


class LinkAdmin(admin.ModelAdmin):
      list_display = ('title', 'is_active',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Link, LinkAdmin)
