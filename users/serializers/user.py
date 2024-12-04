from rest_framework import serializers;
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'Password is required.',
        'blank': 'Password cannot be blank.',
    })
    username = serializers.CharField(required=True, error_messages={
         'required': 'Username is required',
         'black': 'Username cannot be blank',
         'blank': 'Username cannot be left blank',
    })
    email = serializers.EmailField(required=True, error_messages={
         'required': 'Email is required',
         'invalid': 'Email is invalid',
         'blank': 'Email cannot be left blank',
    })

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        """Check if the username already exists."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken. Please choose a different one.")
        return value

    def validate_email(self, value):
        """Check if the email already exists."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered. Please use a different email address.")
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)