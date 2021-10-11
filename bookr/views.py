from django.shortcuts import render


def profile(request):
    """
    View based function that redirected the authenticated user
    to the profile page.
    """
    return render(request, "profile.html")
