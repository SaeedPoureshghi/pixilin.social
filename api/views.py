from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializer import UserRegisterSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny
from .models import Interest, Skill
# Create your views here.

def index(request):
    return JsonResponse({'message': 'Hello, World!'})

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    data = request.data

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return JsonResponse({'error': 'Please provide all required fields!'}, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username is already taken!'}, status=400)
    
    if User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'Email is already taken!'}, status=400)
    
    serializer = UserRegisterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'User created successfully!'}, status=201)

@api_view(['GET'])
def profile(request):
    user = request.user
    user = UserProfileSerializer(user)
    return JsonResponse({'user': user.data})

@api_view(['GET'])
def interests(request):
    data = request.data
    interests_list = data.get('interests')
    user = request.user

    if interests_list:
        for interest in interests_list:
            
            try:
                interest_obj = Interest.objects.get(name=interest)
            except Interest.DoesNotExist:
                interest_obj = Interest.objects.create(name=interest)

            user.interests.add(interest_obj)
            
        user.save()

        return JsonResponse({'message': 'Interests updated successfully!'}, status=200)
    else:
        return JsonResponse({'error': 'Please provide interests list!'}, status=400)
    
@api_view(['GET'])
def skills(request):
    data = request.data
    skills_list = data.get('skills')
    user = request.user

    if skills_list:
        for skill in skills_list:
            
            try:
                skill_obj = Skill.objects.get(name=skill)
            except Skill.DoesNotExist:
                skill_obj = Skill.objects.create(name=skill)

            user.skills.add(skill_obj)
            
        user.save()

        return JsonResponse({'message': 'Skills updated successfully!'}, status=200)
    else:
        return JsonResponse({'error': 'Please provide skills list!'}, status=400)

@api_view(['GET'])
def search_interests(request):
    # read query string
    query = request.query_params.get('query')
    
    if query:
        interests = Interest.objects.filter(name__istartswith=query)
        interests = [interest.name for interest in interests]
        return JsonResponse({'interests': interests}, status=200)
    else:
        return JsonResponse({'error': 'Please provide query!'}, status=400)
    
@api_view(['GET'])
def search_skills(request):
    # read query string
    query = request.query_params.get('query')
    
    if query:
        skills = Skill.objects.filter(name__istartswith=query)
        skills = [skill.name for skill in skills]
        return JsonResponse({'skills': skills}, status=200)
    else:
        return JsonResponse({'error': 'Please provide query!'}, status=400)