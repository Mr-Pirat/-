from django.urls import path

from . import views

app_name='project'
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('<int:pk>/change/',views.changeView.as_view(), name='change'),
]
