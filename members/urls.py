from django.urls import path
from members.views import *

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("foods/", food_list, name="foods"),
    path('calendar-events/', CalendarEvents.as_view(), name='calendar_events'),
    path('pets/<int:id>/',pets, name='pets'),
    path('dashborad/',dashboard, name='dashboard'),
    path('cart/', cart_detail, name='cart_detail'),
    path('add_to_cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('decrease_quantity/<int:food_id>/', decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<int:food_id>/', increase_quantity, name='increase_quantity'),
    path('remove_from_cart/<int:food_id>/', remove_from_cart, name='remove_from_cart'),
    path('create_order/', create_order, name='create_order'),
    path('order/', order_detail, name='order'),
    path('send_order_email/', send_order_email, name='send_order_email'),
    path('order_history/', order_history, name='order_history'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('add_points/', add_points, name='add_points'),

    path('add_pets/', add_pets, name='add_pets'),
    path('update_pets/<int:id>', update_pets, name='update_pets'),
    path('show_pets/', show_pets, name='show_pets'),
    path('delete_pets/<int:id>', delete_pets, name='delete_pets'),

    path('add_foods/', add_foods, name='add_foods'),
    path('show_foods/', show_foods, name='show_foods'),
    path('update_foods/<int:id>', update_foods, name='update_foods'),
    path('delete_foods/<int:id>', delete_foods, name='delete_foods'),

    path('update_order/<int:id>', update_order, name='update_order'),


    path('password_reset/', ForgotPasswordView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('admin_order/', order_detail_admin, name='admin_order'),
    path('order_history_admin/', order_history_admin, name='order_history_admin'),

    path('ex_points/', exchange_points, name='ex_points'),

    path('add_imagecover/', add_imagecover, name='add_imagecover'),

    path('delete_imagecover/<int:id>/', delete_imagecover, name='delete_imagecover'),

    ]

