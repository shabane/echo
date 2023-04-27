from django.db import models


class Server(models.Model):
    certSha256 = models.TextField(blank=True)
    apiUrl = models.CharField(max_length=255)
    wrapper_ip = models.CharField(max_length=15, default='0.0.0.0')
    wrapper_port = models.CharField(max_length=5, default='443')
    name = models.CharField(max_length=125, default='None')

    def __str__(self) -> str:
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    max_size = models.IntegerField(default=3000)
    usage = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)
    key = models.TextField()
    birth_date = models.DateField(auto_now_add=True)
    exp_date = models.DateField()
    pastebin_link = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
