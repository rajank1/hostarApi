from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse, JsonResponse
from .models import Shows , MostPoplular , Starplus, StarBharat ,Episodes ,User,Slide
from .serializers import ShowsSerializer, MostPoplularSerializer, StarplusSerializer,StarBharatSerializer ,EpisodesSerializer ,UserSerializer,SlideSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.http import HttpResponse
import json


class getCreate(generics.ListCreateAPIView):
    queryset=Shows.objects.all()
    serializer_class=ShowsSerializer


class GetEpisodes(generics.ListCreateAPIView):
    serializer_class = EpisodesSerializer

    def get_queryset(self):
        show_id = self.kwargs['show_id']  # Retrieve the show_id from the URL

        # Filter episodes based on the show_id
        queryset = Episodes.objects.filter(show_id=show_id)
        return queryset




@api_view(['POST','PUT','GET'])
def add_update(request):
    if  request.method == 'POST':
        S=ShowsSerializer(data=request.data)
        if S.is_valid():
             S.save()
             return Response({'Created successfully':True})
        else:
             print(S.error_messages)
             print(S.data)
             return Response({'Created Unsuccessfully':False})
    
    elif request.method == 'PUT':
        id = request.GET.get('id')
        show= Shows.objects.get(show_id=id)
        S=ShowsSerializer(instance=show,data=request.data)

        if S.is_valid():
            S.save()
            return Response({'Updated successfully':True})
        else:
            return Response({'Updated successfully':False})
    
    elif request.method == 'GET':
        show=Shows.objects.all()
        serializer  =ShowsSerializer(show,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def getMostPopular(request):
     if request.method == 'GET':
        most_popular_shows = MostPoplular.objects.all()
        show_ids = [show.show_id for show in most_popular_shows]
        shows = Shows.objects.filter(show_id__in=show_ids)
        serializer = MostPoplularSerializer(shows, many=True)
        return Response(serializer.data)
     
@api_view(['GET'])
def getStarplus(request):
     if request.method == 'GET':
        starplus_shows = Starplus.objects.all()
        show_ids = [show.show_id for show in starplus_shows]
        shows = Shows.objects.filter(show_id__in=show_ids)
        serializer = StarplusSerializer(shows, many=True)
        return Response(serializer.data)
     
@api_view(['GET'])
def getStarBharat(request):
     if request.method == 'GET':
        starBharat = StarBharat.objects.all()
        show_ids = [show.show_id for show in starBharat]
        shows = Shows.objects.filter(show_id__in=show_ids)
        serializer = StarBharatSerializer(shows, many=True)
        return Response(serializer.data)
     



@api_view(['POST'])
def get_most_view(request):
    howmany = request.data.get('howmany')
    my_list = request.data.get('my_list')

    send = []
    for item in my_list:
        result = Episodes.objects.filter(show=item).order_by('-episode_no')[:howmany]
        send.extend(list(result))
    
    print(send)
    
    send = EpisodesSerializer(send, many=True)
    return Response(send.data)



@api_view(['GET'])
def getSlide(request):
     if request.method == 'GET':
        slide = Slide.objects.all()
        # show_ids = [show.show_id for show in slide]
        # shows = Shows.objects.filter(show_id__in=show_ids)
        serializer = SlideSerializer(slide, many=True)
        return Response(serializer.data)
     


@api_view(['POST'])
def user_vrify(request):
    if request.method == 'POST':
        email = request.data.get('mail')
        password = request.data.get('psw')

        try:
            # Check if a user with the provided email exists
            user = User.objects.get(mail=email , password=password)
        except User.DoesNotExist:
            # User with the provided email does not exist
            return HttpResponse("Email or password are wrong", status=400)

        # Check if the provided password matches the user's password
        # if user.check_password(password):
        return HttpResponse("Validation successful", status=200)
        # else:
        #     return HttpResponse("Incorrect password", status=400)
        
@api_view(['POST'])
def add_user(request):
    email = request.data.get('mail')
    print("hello")
    first_name = request.data.get('first_name')
    print(first_name)
    
    try:
     User.objects.get(mail=email)
     return HttpResponse("Email is already registered", status=400)
    except User.DoesNotExist:
        user = UserSerializer(data=request.data)
        if user.is_valid():
          user.save()
          return HttpResponse("Registration successful")
    # print(user.errors)
    return HttpResponse(user.errors,status=400)

