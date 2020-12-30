from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.loginpage,name='loginpage'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutfunc,name='logoutfunc'),
    path('pest/',views.pestcontrol,name='pestctrl'),
    path('bookpest/',views.bookingforpest,name='pstbook')
]