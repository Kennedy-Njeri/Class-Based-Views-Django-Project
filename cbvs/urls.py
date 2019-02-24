from django.urls import path
from . import views




urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('list', views.SchoolListView.as_view(), name='list'),
    path('<pk>', views.SchoolDetailView.as_view(), name='detail')


]