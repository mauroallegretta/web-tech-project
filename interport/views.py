from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User, Group
#from .models import CarouselItem
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login
#from django.contrib.auth import views as auth_views
from .forms import UserForm
from .models import Person

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, PersonSerializer

class UserList(APIView):
	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

class PersonList(APIView):
	def get(self, request):
		persons = Person.objects.all()
		serializer = UserSerializer(persons, many=True)
		return Response(serializer.data)


# Create your views here.

def home(request):
	return render(request, 'interport/home.html',{})

def idea(request):
	return render(request, 'interport/idea.html', {})

def author(request):
	return render(request, 'interport/author.html', {})

def future(request):
	return render(request, 'interport/future.html', {})

def user_profile(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'interport/user_profile.html', {'User': user})

def user_list(request):
	users = User.objects.all()
	return render(request, 'interport/user_list.html', {'users':users})
	
@login_required
def person_list(request):
	persons = Person.objects.all()
	return render(request, 'interport/person_list.html', {'persons':persons})

def register_user(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		#profile_form = ProfileForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(**form.cleaned_data)
			user.save()
			#profile = profile_form.save(commit=False)
			#profile.user = user
			#profile.save()
			return redirect('user_profile', pk=user.pk)
	else:
		form = UserForm()
		#profile_form = ProfileForm()
	return render(request, 'interport/register_user.html', {'form':form})

"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""
# Carousel View
"""

def user_carousel(reqest, pk):
	if request.mehtod == "POST":
		item = get_object_or_404(CarouselItem, pk =pk)
	return render(request, 'interpost/user_carousel.html', {'Item': item})




@login_required
def carousel_creator(request):
	if request.method == "POST":
		form = CarouselItemForm(request.POST, request.FILES)
		if form.is_valid():
			item = CarouselItemForm.save()
			return redirect('user_carousel', pk=item.pk)
	else:
		form = CarouselItemForm(request.POST)
	return render(request, 'interport/create_carousel.html', {'form':form})

"""

"""
def register_user(request):
	if request.method == "POST":
		userform = UserForm(request.POST)
		profileform = ProfileForm(request.POST)
		if userform.is_valid() and profileform.is_valid():
			user = userform.save()
			user.set_password(user.password)			
	else:
		userform = UserForm()
		profileform = ProfileForm()
	return render(request, 'interport/register_user.html', {'userform':userform, 'profileform':profileform})
"""



"""
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

"""

"""
def register(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = UserProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()  # save user to db
            userprofile = form2.save(commit=False)  # create profile but don't save to db
            userprofile.user = user
            userprofile.location = get_the_location_somehow()
            userprofile.save()  # save profile to db

    else:
        form1 = UserCreationForm()
         form2 = UserProfileForm()
    c = {
      'form1':form1,
      'form2':form2,
    }
    c.update(csrf(request))
    return render_to_response("registration/register.html", c)
"""

"""
def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('interport/home.html')
	 else:
	 	return redirect('interport/home.html')
"""


	
