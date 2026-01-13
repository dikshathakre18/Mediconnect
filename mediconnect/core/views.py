from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Request


# ================= HOME / LANDING =================
def home(request):
    return render(request, 'landing.html')


# ================= SELECT REQUEST =================
def select_request(request):
    return render(request, 'select_request.html')


# ================= DONOR DASHBOARD =================
def donor_dashboard(request):
    requests = Request.objects.all()
    return render(request, 'donor_dashboard.html', {
        'requests': requests
    })


# ================= REQUESTER DASHBOARD =================
def requester_dashboard(request):
    # If user is authenticated, show only their requests; otherwise show none
    if request.user.is_authenticated:
        requests = Request.objects.filter(requester=request.user)
    else:
        requests = []

    return render(request, 'requester_dashboard.html', {
        'requests': requests
    })


# ================= CREATE REQUEST =================
@login_required
def create_request(request):
    if request.method == 'POST':
        Request.objects.create(
            requester=request.user,
            request_type=request.POST.get('type'),
            detail=request.POST.get('detail'),
            location=request.POST.get('location')
        )
        return redirect('requester_dashboard')

    return render(request, 'create_request.html')


# ================= UPDATE REQUEST =================
@login_required
def update_request(request, id, status):
    req = get_object_or_404(Request, id=id)
    req.status = status
    req.donor = request.user
    req.save()

    return redirect('donor_dashboard')


# ================= AUTH: LOGIN / REGISTER / LOGOUT =================
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.POST.get('next') or request.GET.get('next')
        # we use email as username
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('requester_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            return render(request, 'register.html', {'error': 'User already exists'})

        user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('home')
