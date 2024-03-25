from django.urls import path
from activity.views import ActivityView



app_name = 'activity'

urlpatterns=[
    path('', ActivityView.as_view(), name='main'),


]