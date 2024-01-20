from django.contrib import admin
from .models import *
from django.utils.html import format_html

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','get_full_name', 'phone_number')

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    get_full_name.short_description = 'Full Name'

class FoodAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price','stock','suggested','display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" style="width: auto; height: 80px; border-radius: 12px; border:1px solid;" />', obj.img.url)

class PetAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age','sex','breed','date_time','display_image')

    def display_image(self, obj):
        if obj.profile:
            return format_html('<img src="{}" style="width: auto; height: 80px; border-radius: 12px; border:1px solid;" />', obj.profile.url)
        else:
            return format_html('<img src="{}" style="width: auto; height: 80px; border-radius: 12px; border:1px solid;" />', 'no image')

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('user','get_full_name',)

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name} "

    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('get_user_name','get_full_name','food','quantity','total_price',)

    def get_user_name(self, obj):
        return f"{obj.cart.user} "

    def get_full_name(self, obj):
        return f"{obj.cart.user.first_name} {obj.cart.user.last_name} "
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_user_name','get_full_name','items','is_cancelled','is_paid','total_price',)

    def get_user_name(self, obj):
        return f"{obj.cart.user} "

    def get_full_name(self, obj):
        return f"{obj.cart.user.first_name} {obj.cart.user.last_name} "
    
class NewAdmin(admin.ModelAdmin):
    list_display = ('headline','desc',)


class PointAdmin(admin.ModelAdmin):
    list_display = ('user','total_points',)


class ImageCoverAdmin(admin.ModelAdmin):
    list_display = ('id','display_image')

    def display_image(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="width: auto; height: 80px; border-radius: 12px; border:1px solid;" />', obj.img.url)
        else:
            return format_html('<img src="{}" style="width: auto; height: 80px; border-radius: 12px; border:1px solid;" />', 'no image')

    
admin.site.register(New,NewAdmin)
admin.site.register(Pet,PetAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Point,PointAdmin)
admin.site.register(ImageCover,ImageCoverAdmin)


