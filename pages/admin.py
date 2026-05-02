from django.contrib import admin
from . models import Member , Product
# Register your models here.
# admin.site.register(Member)
admin.site.register(Product)
# pw blabla123
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # أضف اسم الحقل هنا ليكون للقراءة فقط
    readonly_fields = ('date',)