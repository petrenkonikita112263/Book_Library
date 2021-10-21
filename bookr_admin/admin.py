from django.contrib import admin


class BookrAdmin(admin.AdminSite):
    site_header = "Bookr administration"
    logout_template = "admin/logout.html"
