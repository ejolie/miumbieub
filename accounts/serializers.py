from rest_framework import serializers
from .models import User
from movies.serializers import RatingSerializer


class UserSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(Many=True, read_only=True)
    
    class Meta:
        model = User
        fields = "__all__"
