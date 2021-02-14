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


class RoomListView(View):

    def get(self, request):
        room = Room.objects.all()
        return render(request, 'room_list.html', {'room': room})


class DeleteRoomView(View):

    def get(self, request, id):
        Room.objects.filter(pk=id).delete()
        return redirect('/room')

class ModifyRoomView(View):

    def get(self, request, id):
        chosen_room = Room.objects.get(pk=id)
        return render(request, 'modify_room.html', {'chosen_room': chosen_room})

    def post(self, request, id):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        projector = bool(request.POST.get('projector'))
        all_room_names = Room.objects.values_list('name')
        if name == "" or int(capacity) <= 0 or name in all_room_names:
            raise Exception("Wrong data")
        Room.objects.filter(pk=id).update(name=name, capacity=capacity, projector=projector)
        return redirect('/room')
