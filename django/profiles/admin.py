from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Profile, Link


class ProfileAdmin(ModelAdmin):
    list_display = ('get_account', 'title', 'is_active',)

    def get_account(self, obj):
        return obj.account.first_name + ' ' + obj.account.last_name

    get_account.admin_order_field  = 'account' 
    get_account.short_description = 'Account Name'


class LinkAdmin(ModelAdmin):
    list_display = ('get_profile', 'title', 'is_active',)

    def get_profile(self, obj):
        return obj.profile.title

    get_profile.admin_order_field  = 'profile' 
    get_profile.short_description = 'Profile'

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Link, LinkAdmin)
