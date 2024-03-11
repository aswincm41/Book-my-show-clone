from django.shortcuts import render,redirect
from .models import Card 
from .forms import MovieForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def index(request):
    movie=Card.objects.all()
    context={
        'movie_list':movie}
    
    return render(request,'index.html',context)




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful sign-in
        else:
            # Handle invalid credentials
            return render(request, 'signin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to sign-in page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def ad(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        background_image = request.FILES['background_image']  # Get background image
        a = Card(name=name, description=description, year=year, image=image, background_image=background_image)
        a.save()

    return render(request, 'ad.html')


def detalis(request,movie_id):
    movie=Card.objects.get(id=movie_id)
    return render(request,'detalis.html',{'movie':movie})


def delete(request,id):
    if request.method == "POST":
        movie=Card.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")


from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm  # Import your MovieForm

def update(request, movie_id):
    movie = get_object_or_404(Card, pk=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)  # Removed duplicate request.POST
        if form.is_valid():
            form.save()
            return redirect('/', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'update.html', {'form': form, 'movie': movie})
