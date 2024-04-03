from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username','first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):

    interests = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'profile_photo', 'bio', 'interests','skills']
        read_only_fields = ['email', 'username']

    def get_interests(self, obj):
        return obj.interests.values_list('name', flat=True)
    
    def get_skills(self, obj):
        return obj.skills.values_list('name', flat=True)