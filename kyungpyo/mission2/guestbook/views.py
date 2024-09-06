from django.shortcuts import render, redirect
from .models import GuestbookEntry
from .forms import GuestbookEntryForm

# 방명록 목록을 보여주는 뷰
def index(request):
    entries = GuestbookEntry.objects.all().order_by('-created_at')  # 최신순으로 정렬
    return render(request, 'guestbook/index.html', {'entries': entries})

# 방명록 항목을 추가하는 뷰
def add_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm()
    return render(request, 'guestbook/add_entry.html', {'form': form})
