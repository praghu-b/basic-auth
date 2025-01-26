from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from utils import connect_db
from pymongo.errors import PyMongoError
from datetime import datetime, timedelta
from bson import ObjectId

# Connecting the centralized db
db = connect_db()
users_collections = db['users']

def generate_auth_tokens(user):
    refresh = RefreshToken()
    refresh['email'] = user['email']
    refresh['password'] = user['password']
    return refresh


@api_view(['POST'])
def login_user(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Missing fields either email or password'}, status=406)
        
        user = users_collections.find_one({"email": email})

        if not user:
            return Response({'message': 'User doest not exist!'}, status=status.HTTP_401_UNAUTHORIZED)
        elif user['password'] != password:
            return Response({'message': 'Incorrect Password!'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh_token = generate_auth_tokens(user)
        access_token = refresh_token.access_token
        
        user['_id'] = str(user['_id'])
        response =  Response({'message': 'Login Successful!', 'user': user }, status=status.HTTP_202_ACCEPTED)

        response.set_cookie(
            'access_token',
            access_token,   
            httponly=True,            
            secure=True,  # Must be True in production
            max_age=timedelta(days=1),
            samesite='None',
        )

        response.set_cookie(
            'refresh_token',
            refresh_token,   
            httponly=True,            
            secure=True,  # Must be True in production
            max_age=timedelta(days=7),
            samesite='None',
        )

        return response
    
    except Exception as e:
        return Response({'message': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)


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