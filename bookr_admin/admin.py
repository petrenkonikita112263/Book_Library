from django.contrib import admin


class BookrAdmin(admin.AdminSite):
    site_header = "Bookr administration"


admin_site = BookrAdmin(name="bookr_admin")
