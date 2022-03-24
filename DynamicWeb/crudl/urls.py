from django.urls import path
from . import views

urlpatterns = [
    path('new',views.hai),
    path('',views.showing),
    path('<int:unique>',views.reading),
    path('new/<int:key>',views.hai),
    path('del/<int:pos>',views.remove)
]