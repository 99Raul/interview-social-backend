from rest_framework import serializers
from .models import Profile ,Relationship


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'user','email','friends','country']

# class RelationshipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Relationship
#         fields = ['']