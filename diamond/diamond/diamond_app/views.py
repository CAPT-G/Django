from django.shortcuts import render
from .forms import RegistrationForm
from .models import UserProfile
from django.core.mail import send_mail
import random

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Generate random 6-digit verification code
            verification_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            # Store email and verification code securely
            user_profile = UserProfile.objects.create(email=email, verification_code=verification_code)
            # Send email confirmation
            send_mail(
                'Email Verification',
                f'Your verification code is: {verification_code}',
                'your@example.com',
                [email],
                fail_silently=False,
            )
            return render(request, 'registration_success.html')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
