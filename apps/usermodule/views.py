# apps/usermodule/views.py

from django.shortcuts import render

# تعريف دالة profile_view
def profile_view(request):
    return render(request, 'profile.html')

