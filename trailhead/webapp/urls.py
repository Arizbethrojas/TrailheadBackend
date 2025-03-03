#here is where we will place different URL routes and then connect them to our views 
from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TripCreate, SubclubList, RegisterTrip, ViewRegistrationsByStudent, RegisterStudent, StudentProfileView, StudentTripsView, SubclubTripsView, RegisterWaitlist, MarkerListCreateView, BlockedUserList, StudentListView
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt


# list of our paths
urlpatterns = [
    path('api/student/current/', StudentProfileView.as_view()),
    path('api/student/<int:student_id>/', StudentProfileView.as_view(), name='get-name-by-id'),
    path('api/student/<int:student_id>/trips/', StudentTripsView.as_view()),
    path('api/subclub/<int:subclub_id>/trips/', SubclubTripsView.as_view()),
    path("", views.home, name ="home"), #this is an empty path to the base URL of our website
    path("todos/", views.todos, name = "Todos"),
    path("api/trips/", TripCreate.as_view(), name='trip-create'),
    path("trips/create/", views.create_trip, name="create_trip"),
    path("api/subclubs/", SubclubList.as_view(), name="subclub-list"),
    path("api/register_trip/", RegisterTrip.as_view(), name="register_trip"),
    path("api/register_waitlist/", RegisterWaitlist.as_view(), name="register_waitlist"),
    path("api/waitlist/<int:trip_id>/", RegisterWaitlist.as_view(), name='waitlist'),
    path("api/waitlist/remove/", RegisterWaitlist.as_view(), name='remove_waitlist'),
    path("api/registrations/<int:trip_id>/", RegisterTrip.as_view(), name='trippees'),
    path('api/trip-registrations/student/<int:student_id>/', ViewRegistrationsByStudent.as_view(), name='view_registrations_by_student'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('api/sign_up/', csrf_exempt(views.sign_up), name='sign_up'),
    path('api/markers/', MarkerListCreateView.as_view(), name='marker-list-create'),
    path("api/register/", views.RegisterStudent, name="register-student"),  
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('api/blocked-users/', BlockedUserList.as_view(), name='blocked-user-list'),
    path('api/blocked-users/remove/', BlockedUserList.as_view(), name='unblock-user'),
    path('api/students/', StudentListView.as_view(), name='students-list'),
]