from django.contrib import admin

class BookstoreAdminArea(admin.AdminSite):
    site_header = 'Bookstore Admin Area'

bookstore_site = BookstoreAdminArea(name='BookstoreAdmin')
