from django.shortcuts import render

def login_view(request):
    return render(request, "login.html")

def dashboard_view(request):
    return render(request, "dashboard.html")

def chat_view(request, room_id):
    return render(request, "chat.html", {"room_id": room_id})
