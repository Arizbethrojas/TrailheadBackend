from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, Trip, Subclub
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from .serializer import TripSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets

@api_view(['GET'])
def trip_detail(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    except Trip.DoesNotExist:
        return Response({'error': 'Trip not found'}, status=404)


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



@api_view(['GET'])
def trip_detail(request, trip_id):
    try:
        trip = Trip.objects.get(id=trip_id)
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    except Trip.DoesNotExist:
        return Response({'error': 'Trip not found'}, status=404)
    
class TripViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


