from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils import connect_db
from pymongo.errors import PyMongoError
from datetime import datetime
from bson import ObjectId

# Connecting the centralized db
db = connect_db()
users_collections = db['users']


@api_view(['POST'])
def login_user(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Missing fields either email or password'}, status=406)
        
        user = users_collections.find_one({"email": email})

        if not user:
            return Response({'message': 'User doest not exist!'})
        
        user['_id'] = str(user['_id'])
        
        return Response({'message': 'Login Successful!', 'user': user}, status=status.HTTP_202_ACCEPTED)
    except:
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
        return Response({'message': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)