from rest_framework import serializers

from django.contrib.auth.models import User
from . models import blog,likes
class blogser(serializers.ModelSerializer):
    # user=serializers.CharField(read_only=True)
    class Meta:
        model=blog
        fields='__all__'

class likeser(serializers.ModelSerializer):
    # user=serializers.CharField(read_only=True)
    class Meta:
        model=likes
        # fields=['likes_total_count']
        fields='__all__'
class userser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'