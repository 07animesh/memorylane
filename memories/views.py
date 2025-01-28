from django.shortcuts import render, redirect, get_object_or_404
from .models import Memory

def index(request):
    memories = Memory.objects.all()

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        caption = request.POST.get('caption')
        date = request.POST.get('date')

        # Create and save a new memory
        Memory.objects.create(image=photo, caption=caption, date=date)
        return redirect('index')

    return render(request, 'memories/index.html', {'memories': memories})

def delete_memory(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    memory.delete()  # Delete the memory object
    return redirect('index')  # Redirect back to the index page
