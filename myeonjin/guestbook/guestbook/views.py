from django.shortcuts import render, redirect
from .models import GuestbookEntry

def guestbook_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        context = request.POST.get('context')


        if name and context:
            GuestbookEntry.objects.create(name=name, context=context)
            return redirect('guestbook')
    
    entries = GuestbookEntry.objects.all()
    return render(request, 'guestbook.html', {'entries': entries})