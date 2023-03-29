"""
@login_required(login_url='/login')
def create_room(request):
    topics = Topic.objects.all()
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        topic_name = request.POST.get('topic')
        topic, created = Topic
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            form.save()
            return redirect('home')
    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)



@login_required(login_url='/login')
def updateroom(request, pk):
    room = Room.objects.get(id= pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('You are not allowed')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

"""