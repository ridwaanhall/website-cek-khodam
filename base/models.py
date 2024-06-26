from django.db import models


class ListKhodam(models.Model):
    id = models.AutoField(primary_key=True)
    nama_khodam = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nama_khodam
