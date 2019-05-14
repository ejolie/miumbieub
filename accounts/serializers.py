from rest_framework import serializers
from .models import User
from movies.serializers import RatingSerializer


class UserSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    from_user = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'ratings',
            'from_user',
        )
