from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import  smart_bytes,smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from .utils import Util

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric characters'
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token =serializers.CharField(max_length=555)
    class Meta:
        model=User
        fields=['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }


# class LoginSerializer(serializers.ModelSerializer):
#     email=serializers.EmailField(max_length=255, min_length=3)
#     password=serializers.CharField(max_length=68, min_length=6, write_only=True)
#     username=serializers.CharField(max_length=255, min_length=3, read_only=True)
#     # tokens=serializers.CharField(max_length=68, min_length=6, read_only=True)
#     tokens=serializers.SerializerMethodField()

#     def get_tokens(self,obj):
#         user=User.objects.get(email=obj['email'])
#         return {
#             'access':user.tokens()['access'],
#             'refresh': user.tokens()['refresh']
#         }
#     class Meta:
#         model =User
#         fields=['email', 'password', 'username', 'tokens']


#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         password = attrs.get('password', '')



#         user=auth.authenticate(email=email, password=password)
#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')

#         if not user.is_active:
#             raise AuthenticationFailed('Account disabled, contact admin')
#         if not user.is_verified:
#             raise AuthenticationFailed('Email is not verified')

#         return {
#             'email': user.email,
#             'username':user.username,
#             'tokens':user.tokens()
#         }
        # return super().validate(attrs)

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email=serializers.EmailField(min_length=2)
    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields=['email']




class SetNewPasswordSerializer(serializers.Serializer):
    password=serializers.CharField(min_length=6,max_length=68, write_only=True)
    token=serializers.CharField(min_length=1, write_only=True)
    uidb64=serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields=['password', 'token', 'uidb64']


    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id=force_str(urlsafe_base64_decode(uidb64))
            user= User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            user.set_password(password)

            user.save()
        except  Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)




        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):

        refresh = serializers.CharField()

        default_error_messages = {
            'bad_token':("Token is expired or invalid")
        }

        def validate(self, attrs):
            self.token =attrs['refresh']

            return attrs
        def save(self, **kwargs):
            try:

               RefreshToken(self.token).blacklist()
            except TokenError:
                self.fail('bad_token')
    # def validate(self, attrs):

    #         email=attrs['data'].get('email','')
    #         if User.objects.filter(email=email).exists():
    #             user= User.objects.get(email=email)
    #             uidb64=urlsafe_base64_encode(user.id)
    #             token = PasswordResetTokenGenerator().make_token(user)
    #             current_site = get_current_site(request=attrs['data'].get('request')).domain
    #             relativeLink = reverse('password-reset-confirm', kwargs={'uidb64':uidb64,'token':token})
    #             absurl = f'http://{current_site}{relativeLink}'
    #             email_body = 'Hello \n'+ ' Use the link below to reset your email \n' + absurl
    #             data = {'email_body': email_body, 'to_email': user.email,
    #                     'email_subject': 'Reset your password'}

    #             Util.send_email(data)

    #             return attrs


    #         return super().validate(attrs)