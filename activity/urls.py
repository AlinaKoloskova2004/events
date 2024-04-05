from django.urls import path
from activity.views import ActivityView, AboutView
from . import views


app_name = 'activity'

urlpatterns=[
    path('', ActivityView.as_view(), name='main'),
    path('types/', views.events, name='types'),
    path('events/<str:type>/', views.events_in_type, name='events_in_type'),
    path('detail/<int:event_id>/<str:user_id>', views.event_detail, name='event_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('profile_user/',  views.view_profile, name='profile_user'),
    path('profile_user/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile_user/create_profile/', views.create_profile, name='create_profile'),
    path('profile_user/create_profile/success', views.success, name='success'),
    path('events_list/', views.events_list, name='events_list'),
]