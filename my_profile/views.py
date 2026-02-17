from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from register.models import Profile

@login_required
def profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    context={
        "user_obj":user,
        "profile":profile
    }
    return render(request,"profile.html",context)
