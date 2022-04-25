from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.auth),
    path('out',views.out),
    path('new',views.hai),
    path('home',views.showing),
    path('<int:unique>',views.reading),
    path('new/<int:key>',views.hai),
    path('del/<int:pos>',views.remove),
    path('find',views.short),
    path('found',views.handleShort),
    path('api/newone',views.newCorp),
    path('api/',views.listAll),
    path('api/<data>',views.individual),
    path('api/byid/<int:data>',views.individualsId),
    path('api/del/<int:key>',views.removing),
    path('api/up/<int:id>',views.upCorp),
    path('api/delob',views.removingByObject),
]