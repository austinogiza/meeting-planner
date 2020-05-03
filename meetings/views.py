from django.shortcuts import render, get_object_or_404,redirect
from datetime import  time
from .models import Meetings, Room
from django.forms import  modelform_factory

# Create your views here.

def home(request):
    meetings = Meetings.objects.all()
    context ={
        'meetings' : meetings
    }

    return render(request, 'home.html', context)


def details(request, id):
    meetings = get_object_or_404(Meetings, pk=id)
    context = {
        'meetings': meetings
    }

    return render(request, 'detail.html', context)


def room(request):
    room = Room.objects.all()
    context ={
        'room' : room
    }
    return render(request, 'room.html', context)


MeetingForm = modelform_factory(Meetings, exclude=[])

def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/new/")
    else: 
        form = MeetingForm()
    return render(request, 'new.html', {'form':form})