﻿from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Section, Group, Item, Image, Area, Profile


class ImageInline(AdminImageMixin, admin.StackedInline):
    model = Image
    extra = 5


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', 'group', 'area', 'user', 'is_active', 'posted', 'updated')
    list_filter = ('area', 'group', 'is_active', 'posted',)
    search_fields = ('title', 'description', 'user__email')
    inlines = [ImageInline]


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', 'slug', 'section', 'count')
    list_filter = ('section',)
    search_fields = ('title', 'section__title')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AreaAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    prepopulated_fields = {'slug': ('title',)}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')


admin.site.register(Area, AreaAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Profile, ProfileAdmin)
