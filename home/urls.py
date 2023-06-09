from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Pages
    path('', views.index, name="index"),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('about-us/', views.about_us, name='about-us'),
    path('profile/', views.author, name='profile'),

    # Plans

    path('gst', views.GST, name='gst'),
    path('accounting', views.accounting, name='accounting'),
    path('Business_Incorporation', views.Business_Incorporation, name='Business_Incorporation'),
    path('Incometax/', views.Incometax, name='Incometax'),
    path('PMS', views.PMS, name='PMS'),
    path('DSC', views.DSC, name='DSC'), 
    path('Compliance', views.Compliance, name='Compliance'),
    path('Trademark', views.Trademark, name='Trademark'),

    path('save_payment_details',views.save_payment_details,name='save_payment_details'),


    # path('', webprint, name='webprint'),
    path('ccavResponseHandler', views.ccavResponseHandler, name='ccavResponseHandler'),
    path('checkout', views.checkout, name='checkout'),

    # path('checkout', views.checkout, name='checkout'),



    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Sections
    path('presentation/', views.presentation, name='presentation'),
    path('page-header/', views.page_header, name='page_header'),
    path('features/', views.features, name='features'),
    path('navbar/', views.navbars, name='navbar'),
    path('nav-tabs/', views.nav_tabs, name='nav_tabs'),
    path('pagination/', views.pagination, name='pagination'),
    path('forms/', views.forms, name='forms'),
    path('inputs/', views.inputs, name='inputs'),
    path('avatars/', views.avatars, name='avatars'),
    path('badges/', views.badges, name='badges'),
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs'),
    path('buttons/', views.buttons, name='buttons'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('progress-bars/', views.progress_bars, name='progress_bars'),
    path('toggles/', views.toggles, name='toggles'),
    path('typography/', views.typography, name='typography'),
    path('alerts/', views.alerts, name='alerts'),
    path('modals/', views.modals, name='modals'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('payment/', views.payment, name='payment'),
    path('payment_response/', views.payment_response, name='payment_response'),

    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_cancel/', views.payment_cancel, name='payment_cancel'),

]
