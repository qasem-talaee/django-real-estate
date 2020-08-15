from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class UserExtraAdmin(admin.ModelAdmin):
    def image_user(self, obj):
        return mark_safe('<img src="{image}" class="img-fluid" width="30%" />'.format(image=obj.image.url))
    image_user.short_description = 'Image'
    list_display = ('name', 'image_user', 'job')
    search_fields = ('name', 'email',)
    list_filter = ('job',)
    ordering = ('-id',)
    list_per_page = 30

class BlogAdmin(admin.ModelAdmin):
    def image_blog(self, obj):
        return mark_safe('<img src="{image}" class="img-fluid" width="50%" />'.format(image=obj.image.url))
    def url_blog(self, obj):
        return mark_safe('<a href="/blog-detail/{thisurl}/" class="button" target="_blank">View</a>'.format(thisurl=obj.url))
    image_blog.short_description = 'Image'
    url_blog.short_description = 'View'
    list_display = ('title', 'image_blog', 'url_blog', 'writer', 'date')
    search_fields = ('title',)
    list_filter = ('writer',)
    ordering = ('-id',)
    list_per_page = 30

class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('-id',)
    list_per_page = 30

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('-id',)
    list_per_page = 30

class PropertyAdmin(admin.ModelAdmin):
    def url_property(self, obj):
        return mark_safe('<a href="/property-detail/{thisid}/" class="button" target="_blank">View</a>'.format(thisid=obj.id))
    url_property.short_description = 'View'
    list_display = ('title', 'active', 'agent', 'url_property', 'city', 'status', 'address', 'property_type', 'home_area', 'price')
    search_fields = ('title', 'address', 'home_area', 'price')
    list_filter = ('agent', 'active', 'city', 'status', 'property_type', 'baths', 'garage', 'bed_room')
    ordering = ('-id',)
    list_per_page = 30

class AgentContactAdmin(admin.ModelAdmin):
    def prop_admin(self, obj):
        property = Property.objects.filter(id=obj.property.id)
        for i in property:
            id = i.id
        return mark_safe('<a class="button" target="_blank" href="/property-detail/{id}/">View</a>'.format(id=id))
    prop_admin.short_description = 'View Property'
    list_display = ('agent', 'property', 'prop_admin', 'name', 'email', 'phone', 'date', 'status')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('agent', 'status',)
    ordering = ('-id',)
    list_per_page = 30

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'status')
    search_fields = ('name', 'email', 'phone',)
    list_filter = ('status',)
    ordering = ('-id',)
    list_per_page = 30

admin.site.register(UserExtra, UserExtraAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(AgentContact, AgentContactAdmin)
admin.site.register(Contact, ContactAdmin)