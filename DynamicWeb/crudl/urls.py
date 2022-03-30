from django.urls import include, path
from . import views

urlpatterns = [
    path('new',views.hai),
    path('',views.showing),
    path('<int:unique>',views.reading),
    path('new/<int:key>',views.hai),
    path('del/<int:pos>',views.remove),
    path('find',views.short),
    path('found',views.handleShort),
    path('api/newone',views.newCorp),
    path('api/',views.listAll),
    path('api/<int:data>',views.individual),
    path('api/del/<int:key>',views.removing),
]