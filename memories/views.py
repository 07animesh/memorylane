from django.shortcuts import render, redirect, get_object_or_404
from .models import Memory

def index(request):
    memories = Memory.objects.all().order_by('-date')  # Order by latest first

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        caption = request.POST.get('caption')
        date = request.POST.get('date')

        if photo and caption and date:  # Ensure all fields are filled
            Memory.objects.create(image=photo, caption=caption, date=date)
        
        return redirect('index')  # Redirect to refresh the page

    return render(request, 'memories/index.html', {'memories': memories})

def delete_memory(request, memory_id):
    memory = get_object_or_404(Memory, id=memory_id)
    memory.delete()
    return redirect('index')
