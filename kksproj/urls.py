from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('page2',views.create, name='create'),
    path('page3',views.textedit, name='textedit'),
]
