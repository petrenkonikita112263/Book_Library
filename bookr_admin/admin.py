from django.contrib import admin
from django.contrib.auth.admin import User


class BookrAdmin(admin.AdminSite):
    site_header = "Bookr administration"


admin_site = BookrAdmin(name="bookr_admin")
admin_site.register(User)
