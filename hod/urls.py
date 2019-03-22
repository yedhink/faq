from django.urls import path,include

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('success',views.on_submit,name="on_submit"),
    path('login_success',views.login_success,name="login_success"),
    path('logout',views.logout,name="logout"),
    path('hod/<int:hod_id>/',views.hod_view,name="hod_view"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hod/<int:hod_id>/<int:q_id>/',views.del_item,name="del_item"),
    path('send_query_response',views.send_query_response,name="send_query_response")
]