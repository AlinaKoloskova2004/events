from django.urls import path
from activity.views import ActivityView
from . import views


app_name = 'activity'

urlpatterns=[
    path('', ActivityView.as_view(), name='main'),
    path('types/', views.events, name='types'),
    path('events/<str:type>/', views.events_in_type, name='events_in_type'),
]