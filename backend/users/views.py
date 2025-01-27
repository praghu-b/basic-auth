from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.exceptions import AuthenticationFailed
from utils import connect_db
from pymongo.errors import PyMongoError
from datetime import datetime, timedelta
from bson import ObjectId

db = connect_db()
users_collections = db['users']


def generate_auth_tokens(user):
    refresh = RefreshToken()
    refresh['email'] = user['email']
    refresh['password'] = user['password']
    return refresh


@api_view(['POST'])
def validate_token(request):
    access_token = request.COOKIES.get('access_token')
    if not access_token:
        raise AuthenticationFailed('Token not found')
    
    try:
        AccessToken(access_token)
    except Exception as e:
        raise AuthenticationFailed(f'{e}')
    
    return Response({'message': "You have access to this route!"}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def refresh_token(request):
    refresh_token = request.COOKIES.get('refresh_token')
    if not refresh_token:
        raise AuthenticationFailed('Token not found')
    
    try:
        refresh = RefreshToken(refresh_token)
        new_access_token = str(refresh.access_token)

        response = Response({'message': 'Token refreshed!'})
        response.set_cookie(
            'access_token',
            new_access_token,   
            httponly=False,            
            secure=True,
            max_age=timedelta(days=1),
            samesite='None',
        )

        return response
    except Exception as e:
        raise AuthenticationFailed(f'{e}')
    

@api_view(['POST'])
def logout_user(request):
    try:
        response = Response({'message': 'User Logged Out Successfully!'}, status=status.HTTP_200_OK)
        
        response.delete_cookie('access_token', path='/')
        response.delete_cookie('refresh_token', path='/')

        return response
    except Exception as e:
        Response({'message': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_user(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Missing fields either email or password'}, status=406)
        
        user = users_collections.find_one({"email": email})

        if not user:
            return Response({'message': 'User does not exist!'}, status=status.HTTP_401_UNAUTHORIZED)
        elif user['password'] != password:
            return Response({'message': 'Incorrect Password!'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh_token = generate_auth_tokens(user)
        access_token = refresh_token.access_token
        
        user['_id'] = str(user['_id'])
        response =  Response({'message': 'Login Successful!', 'user': user }, status=status.HTTP_202_ACCEPTED)

        response.set_cookie(
            'access_token',
            access_token,   
            httponly=False,            
            secure=True,
            max_age=timedelta(days=1),
            samesite='None',
        )

        response.set_cookie(
            'refresh_token',
            refresh_token,   
            httponly=False,            
            secure=True,
            max_age=timedelta(days=7),
            samesite='None',
        )

        return response
    
    except Exception as e:
        return Response({'message': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_user(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not name or not email or not password:
            return Response({'message': 'All fields are required!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        existingUser = users_collections.find_one({'email': email})

        if existingUser:
            return Response({'message': 'User with the email id already exists!'}, status=status.HTTP_403_FORBIDDEN)
        
        users_collections.insert_one({ "name": name, "email": email, "password": password, "createdAt": datetime.now(), "updatedAt": datetime.now() })

        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)

    except PyMongoError as e:
        print(f'Error: {e}')
        return Response({'message': 'Error storing the data!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    except Exception as e:
        print(f'Error: {e}')
        return Response({'message': 'Something went wrong!', 'error': e}, status=status.HTTP_400_BAD_REQUEST)