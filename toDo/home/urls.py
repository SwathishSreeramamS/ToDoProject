from django.urls import path
from . import views

urlpatterns=[
    path('',views.indexPage,name='index'),
    path('add/',views.addToDo,name='add'),
    path('delete/<str:id>',views.deleteToDo,name='delete'),
    path('finished/<str:id>',views.finishedToDo,name='finished'),
    path('deleteall/',views.deleteAllToDo,name='deleteall')
]