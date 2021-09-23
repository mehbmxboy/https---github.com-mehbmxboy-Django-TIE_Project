from django.contrib import admin

# Register your models here.
from . models import Userquest, Usercomment, Contactus, Likepost


class questonadmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class commentadmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class contactusadmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class likepostadmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Userquest, questonadmin)

admin.site.register(Usercomment, commentadmin)

admin.site.register(Contactus, contactusadmin)

admin.site.register(Likepost, likepostadmin)
