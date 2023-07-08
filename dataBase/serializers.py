from rest_framework import serializers
from .models import Shows,Episodes ,User,Slide

class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shows
        fields='__all__'

class MostPoplularSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shows
        fields='__all__'

class StarplusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shows
        fields='__all__'

class StarBharatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shows
        fields='__all__'


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model=Slide
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Episodes
        fields='__all__'

