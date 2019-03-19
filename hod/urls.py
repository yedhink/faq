from django.urls import path,include

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('success',views.on_submit,name="on_submit"),
    path('hod/<int:hod_id>/',views.hod_view,name="hod_view"),
    path('accounts/', include('django.contrib.auth.urls')),
]