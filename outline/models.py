from django.db import models


class Channel(models.Model):
    username = models.CharField(max_length=32, null=True, unique=True)
    name = models.CharField(max_length=50, default='admin')

    def __str__(self) -> str:
        return self.name


class Server(models.Model):
    certSha256 = models.TextField(blank=True)
    apiUrl = models.CharField(max_length=255)
    wrapper_ip = models.CharField(max_length=15, default='0.0.0.0')
    wrapper_port = models.CharField(max_length=5, default='443')
    name = models.CharField(max_length=125, default='None')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    max_size = models.IntegerField(default=3000)
    usage = models.IntegerField(default=0, blank=True)
    enabled = models.BooleanField(default=True)
    key = models.TextField(blank=True)
    birth_date = models.DateField(auto_now_add=True)
    exp_date = models.DateField()
    pastebin_link = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
    outline_id = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
