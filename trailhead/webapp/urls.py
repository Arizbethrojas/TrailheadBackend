#here is where we will place different URL routes and then connect them to our views 
from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TripCreate, SubclubList, RegisterTrip, ViewRegistrationsByStudent, StudentProfileView, StudentTripsView, SubclubTripsView, RegisterWaitlist, GetWaitlist, GetTrippees
from . import views
from django.contrib.auth import views as auth_views
from .views import get_csrf_token


# list of our paths
urlpatterns = [
    path('api/csrf-token/', get_csrf_token, name='csrf-token'),
    path('api/student/current/', StudentProfileView.as_view()),
    path('api/student/<int:student_id>/trips/', StudentTripsView.as_view()),
    path('api/subclub/<int:subclub_id>/trips/', SubclubTripsView.as_view()),
    path("", views.home, name ="home"), #this is an empty path to the base URL of our website
    path("todos/", views.todos, name = "Todos"),
    path("api/trips/", TripCreate.as_view(), name='trip-create'),
    path("trips/create/", views.create_trip, name="create_trip"),
    path("api/subclubs/", SubclubList.as_view(), name="subclub-list"),
    path("api/register_trip/", RegisterTrip.as_view(), name="register_trip"),
    path("api/register_waitlist/", RegisterWaitlist.as_view(), name="register_waitlist"), 
    path("api/waitlist/<int:trip_id>/", GetWaitlist.as_view(), name='waitlist'),
    path("api/waitlist/remove/", RegisterWaitlist.as_view(), name="remove_waitlist"),
    path("api/trip-registrations/<int:trip_id>/", GetTrippees.as_view(), name='trippees'),
    path('api/trip-registrations/student/<int:student_id>/', ViewRegistrationsByStudent.as_view(), name='view_registrations_by_student'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('sign_up_step1/', views.sign_up_step1, name='sign_up_step1'),
    path('sign_up_step2/', views.sign_up_step2, name='sign_up_step2'),
    path('sign_up_step3/', views.sign_up_step3, name='sign_up_step3'),
]