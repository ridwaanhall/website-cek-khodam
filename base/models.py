from django.db import models


class ListKhodam(models.Model):
    id = models.AutoField(primary_key=True)
    nama_khodam = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nama_khodam

class ResponseLog(models.Model):
    code = models.IntegerField()
    status = models.CharField(max_length=100)
    message = models.TextField()
    name = models.CharField(max_length=255, null=True, blank=True)
    khodam = models.CharField(max_length=255, null=True, blank=True)
    current_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.current_time} - {self.name} - {self.khodam}"
