from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name='BlogAdmin')

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(models.Post, SummerAdmin)
blog_site.register(models.Post, SummerAdmin)



