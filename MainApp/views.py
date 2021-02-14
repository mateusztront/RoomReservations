from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from MainApp.models import Room


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


class NewRoomView(View):

    def get(self, request):
        return render(request, 'new_room.html')

    def post(self, request):
        room_name = request.POST['room_name']
        if room_name == "":
            raise Exception('Room name is empty')
        capacity = request.POST['capacity']
        if int(capacity) < 1:
            raise Exception('wrong capacity')
        pro = request.POST.get('projector', False)
        projector = bool(pro)
        Room.objects.create(name=room_name, capacity=capacity, projector=projector)
        return redirect('/')
