from django.db import models

class GuestbookEntry(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 본문
    author = models.CharField(max_length=100)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일 (자동으로 현재 시간 저장)

    def __str__(self):
        return f"{self.title} by {self.author}"
