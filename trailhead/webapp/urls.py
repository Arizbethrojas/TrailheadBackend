#here is where we will place different URL routes and then connect them to our views 
from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#changing to be djangorestframework
# from djangorestframework import TokenObtainPairView, TokenRefreshView
from .views import TripCreate, SubclubList, RegisterTrip, ViewRegistrationsByStudent
from . import views


# list of our paths
urlpatterns = [
    path("", views.home, name ="home"), #this is an empty path to the base URL of our website
    path("todos/", views.todos, name = "Todos"),
    path("api/trips/", TripCreate.as_view(), name='trip-create'),
    path("trips/create/", views.create_trip, name="create_trip"),
    path("api/subclubs/", SubclubList.as_view(), name="subclub-list"),
    path("api/register_trip/", RegisterTrip.as_view(), name="register_trip"),
    path('api/trip-registrations/student/<int:student_id>/', ViewRegistrationsByStudent.as_view(), name='view_registrations_by_student'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]