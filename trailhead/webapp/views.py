from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, Trip, Subclub
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trip, TripRegistration, Student
from .serializer import TripSerializer, SubclubSerializer, TripRegistrationSerializer

# Create views 
def home(request): 
    return render(request, "home.html")

def todos(request):
    items= TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def create_trip(request):
    if request.method == "POST":
        #Handle form submission
        trip_name = request.POST.get('trip_name')
        trip_date = request.POST.get('trip_date')
        trip_description = request.POST.get('trip_description')
        trip_leader = request.POST.get('trip_leader')
        trip_capacity = request.POST.get('trip_capacity')
        subclub_name = request.POST.get('subclub')

        try:
            subclub = Subclub.objects.get(subclub_name=subclub_name)
        except Subclub.DoesNotExist:
            return render(request, "create_trip.html", {"error": "Subclub not found."})
        except Exception as e:
            return render(request, "create_trip.html", {"error": str(e)})
        
        #create the trip
        new_trip = Trip(
            trip_name = trip_name,
            trip_date = trip_date,
            trip_description = trip_description,
            trip_leader = trip_leader,
            trip_capacity = trip_capacity,
            subclub = subclub
            )
        new_trip.save() #save to the database

        return redirect(home)
    #return the trip creation form on GET request
    return render(request, "create_trip.html")

class TripCreate(APIView):
    #Retrieves all Trip entries 
    #returns them in JSON format.
    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    #creates new post 
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubclubList(APIView):
    def get(self, request):
        subclubs = Subclub.objects.all()
        serializer = SubclubSerializer(subclubs, many=True)
        return Response(serializer.data)
    
class RegisterTrip(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        trip_id = request.data.get('trip_id')

        if not student_id or not trip_id:
            return Response({'error': 'Student ID and Trip ID required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(id=student_id)
            trip = Trip.objects.get(id=trip_id)

            registration = TripRegistration(student=student, trip=trip)
            registration.save()

            serializer = TripRegistrationSerializer(registration)

            return Response({
                'registration_id': serializer.data,
                'message': 'Successfully registered for the trip!'
            }, status=status.HTTP_201_CREATED)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found' }, status=status.HTTP_404_NOT_FOUND)
        except Trip.DoesNotExist:
            return Response({'error': 'Trip not found' }, status=status.HTTP_404_NOT_FOUND)