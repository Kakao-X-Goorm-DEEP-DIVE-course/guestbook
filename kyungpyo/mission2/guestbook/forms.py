from django import forms
from .models import GuestbookEntry

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['title', 'content', 'author']  # 폼에서 사용할 필드 목록
