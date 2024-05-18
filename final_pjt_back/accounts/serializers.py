from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class SignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            id_name = validated_data['id_name'],
            password = validated_data['password'],
            birth = validated_data.get('birth'),
            sex = validated_data.get('sex'),
            main_bank = validated_data.get('main_bank'),
            salary = validated_data.get('salary'),
            asset = validated_data.get('asset'),
            desired_asset = validated_data.get('desired_asset'),
        )
        return user
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': '비밀번호가 일치하지 않습니다.'})
        return data
    
    class Meta:
        model = User
        fields = ['nickname', 'email', 'id_name', 'password', 'password2', 'birth', 'sex', 'main_bank', 'salary', 'asset', 'desired_asset']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserLoginSerializer(serializers.Serializer):
    id_name = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data.get('id_name'), password=data.get('password'))
        if user is None:
            raise serializers.ValidationError('Invalid id_name/password.')
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email', 'birth', 'sex', 'main_bank', 'salary', 'asset', 'desired_asset']