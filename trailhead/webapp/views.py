from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, Trip, Subclub, TripRegistration, Student
from .forms import BasicInfoForm, PersonalDetailsForm, ProfilePreferencesForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsTripLeader
from rest_framework import status
from .serializer import TripSerializer, SubclubSerializer, TripRegistrationSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

# Step 1: Basic Info
def sign_up_step1(request):
    if request.method == "POST":
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Save basic info in the session for later use
            request.session['is_trip_leader'] = form.cleaned_data['is_trip_leader']
            request.session['user_id'] = user.id
            return redirect('sign_up_step2')
    else:
        form = BasicInfoForm()
    return render(request, 'sign_up_step1.html', {'form': form})

# Step 2: Personal Details
def sign_up_step2(request):
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            # Save data in session for the next step
            request.session['allergies'] = form.cleaned_data['allergies']
            request.session['class_year'] = form.cleaned_data['class_year']
            request.session['pronouns'] = form.cleaned_data['pronouns']
            return redirect('sign_up_step3')
    else:
        form = PersonalDetailsForm()
    return render(request, 'sign_up_step2.html', {'form': form})

# Step 3: Profile Preferences
def sign_up_step3(request):
    if request.method == "POST":
        form = ProfilePreferencesForm(request.POST, request.FILES)
        if form.is_valid():
            # Fetch the user
            user = User.objects.get(id=request.session['user_id'])

            # Check if the Student record already exists
            student, created = Student.objects.get_or_create(
                user=user,  # Match on user
                defaults={  # Fields to set if creating a new record
                    'student_name': user.username,
                    'is_trip_leader': request.session.get('is_trip_leader', False),
                    'allergies': request.session.get('allergies', ''),
                    'class_year': request.session.get('class_year', ''),
                    'pronouns': request.session.get('pronouns', '')
                }
            )

            # If the record already exists, update the fields
            if not created:
                student.is_trip_leader = request.session.get('is_trip_leader', False)
                student.allergies = request.session.get('allergies', '')
                student.class_year = request.session.get('class_year', '')
                student.pronouns = request.session.get('pronouns', '')

            # Save the profile picture
            if form.cleaned_data['profile_picture']:
                student.profile_picture = form.cleaned_data['profile_picture']

            # Save favorite subclubs
            student.save()
            student.favorite_subclubs.set(form.cleaned_data['favorite_subclubs'])

            return redirect('home')
    else:
        form = ProfilePreferencesForm()
    return render(request, 'sign_up_step3.html', {'form': form})


class TripLeaderView(APIView):
    permission_classes = [IsTripLeader]

    def get(self, request):
        # Your logic for trip leaders
        return Response({"message": "Welcome, Trip Leader!"}, status=status.HTTP_200_OK)

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

#Get trips that a specific student is on 
class ViewRegistrationsByStudent(APIView):
    def get(self, request, student_id):
        try:
            registrations = TripRegistration.objects.filter(student_id = student_id).select_related('trip')
            trips = [registration.trip for registration in registrations]
            serializer = TripSerializer(trips, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        

from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, Trip, Subclub, TripRegistration, Student
from .forms import BasicInfoForm, PersonalDetailsForm, ProfilePreferencesForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsTripLeader
from rest_framework import status
from .serializer import TripSerializer, SubclubSerializer, TripRegistrationSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

# Step 1: Basic Info
def sign_up_step1(request):
    if request.method == "POST":
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Save basic info in the session for later use
            request.session['is_trip_leader'] = form.cleaned_data['is_trip_leader']
            request.session['user_id'] = user.id
            return redirect('sign_up_step2')
    else:
        form = BasicInfoForm()
    return render(request, 'sign_up_step1.html', {'form': form})

# Step 2: Personal Details
def sign_up_step2(request):
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            # Save data in session for the next step
            request.session['allergies'] = form.cleaned_data['allergies']
            request.session['class_year'] = form.cleaned_data['class_year']
            request.session['pronouns'] = form.cleaned_data['pronouns']
            return redirect('sign_up_step3')
    else:
        form = PersonalDetailsForm()
    return render(request, 'sign_up_step2.html', {'form': form})

# Step 3: Profile Preferences
def sign_up_step3(request):
    if request.method == "POST":
        form = ProfilePreferencesForm(request.POST, request.FILES)
        if form.is_valid():
            # Fetch the user
            user = User.objects.get(id=request.session['user_id'])

            # Check if the Student record already exists
            student, created = Student.objects.get_or_create(
                user=user,  # Match on user
                defaults={  # Fields to set if creating a new record
                    'student_name': user.username,
                    'is_trip_leader': request.session.get('is_trip_leader', False),
                    'allergies': request.session.get('allergies', ''),
                    'class_year': request.session.get('class_year', ''),
                    'pronouns': request.session.get('pronouns', '')
                }
            )

            # If the record already exists, update the fields
            if not created:
                student.is_trip_leader = request.session.get('is_trip_leader', False)
                student.allergies = request.session.get('allergies', '')
                student.class_year = request.session.get('class_year', '')
                student.pronouns = request.session.get('pronouns', '')

            # Save the profile picture
            if form.cleaned_data['profile_picture']:
                student.profile_picture = form.cleaned_data['profile_picture']

            # Save favorite subclubs
            student.save()
            student.favorite_subclubs.set(form.cleaned_data['favorite_subclubs'])

            return redirect('home')
    else:
        form = ProfilePreferencesForm()
    return render(request, 'sign_up_step3.html', {'form': form})


class TripLeaderView(APIView):
    permission_classes = [IsTripLeader]

    def get(self, request):
        # Your logic for trip leaders
        return Response({"message": "Welcome, Trip Leader!"}, status=status.HTTP_200_OK)

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

#Get trips that a specific student is on 
class ViewRegistrationsByStudent(APIView):
    def get(self, request, student_id):
        try:
            registrations = TripRegistration.objects.filter(student_id = student_id).select_related('trip')
            trips = [registration.trip for registration in registrations]
            serializer = TripSerializer(trips, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        

class StudentProfileView(APIView):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            
            # Get registered trips
            registered_trips = Trip.objects.filter(
                tripregistration__student=student
            )
            
            # Get trips where user is leader
            led_trips = Trip.objects.filter(
                trip_leader=student.student_name  # Assuming trip_leader stores the student_name
            )

            return Response({
                'student_name': student.student_name,
                'class_year': student.class_year,
                'pronouns': student.pronouns,
                'allergies': student.allergies,
                'is_trip_leader': student.is_trip_leader,
                'id': student.id,
                'registered_trips': TripSerializer(registered_trips, many=True).data,
                'led_trips': TripSerializer(led_trips, many=True).data
            })
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
        
class StudentTripsView(APIView):
    def get(self, request, student_id):
        try:
            # Get all trip registrations for this student
            registrations = TripRegistration.objects.filter(student_id=student_id)
            
            # Get the related trip data
            trips = []
            for registration in registrations:
                trip = registration.trip
                trips.append({
                    'trip_name': trip.trip_name,
                    'trip_date': trip.trip_date,
                    'trip_leader': trip.trip_leader,
                    'subclub': trip.subclub.subclub_name,
                    'trip_type': trip.trip_type,
                    'trip_level': trip.trip_level
                })
            
            return Response(trips)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SubclubTripsView(APIView):
    def get(self, request, subclub_id):
        try:
            trips = Trip.objects.filter(subclub_id=subclub_id)
            trips_data = []
            
            for trip in trips:
                trips_data.append({
                    'trip_name': trip.trip_name,
                    'trip_date': trip.trip_date,
                    'trip_leader': trip.trip_leader,
                    'trip_capacity': trip.trip_capacity,
                    'trip_type': trip.trip_type,
                    'trip_level': trip.trip_level
                })
            
            return Response(trips_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        
class StudentTripsView(APIView):
    def get(self, request, student_id):
        try:
            # Get all trip registrations for this student
            registrations = TripRegistration.objects.filter(student_id=student_id)
            
            # Get the related trip data
            trips = []
            for registration in registrations:
                trip = registration.trip
                trips.append({
                    'trip_name': trip.trip_name,
                    'trip_date': trip.trip_date,
                    'trip_leader': trip.trip_leader,
                    'subclub': trip.subclub.subclub_name,
                    'trip_type': trip.trip_type,
                    'trip_level': trip.trip_level
                })
            
            return Response(trips)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SubclubTripsView(APIView):
    def get(self, request, subclub_id):
        try:
            trips = Trip.objects.filter(subclub_id=subclub_id)
            trips_data = []
            
            for trip in trips:
                trips_data.append({
                    'trip_name': trip.trip_name,
                    'trip_date': trip.trip_date,
                    'trip_leader': trip.trip_leader,
                    'trip_capacity': trip.trip_capacity,
                    'trip_type': trip.trip_type,
                    'trip_level': trip.trip_level
                })
            
            return Response(trips_data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)