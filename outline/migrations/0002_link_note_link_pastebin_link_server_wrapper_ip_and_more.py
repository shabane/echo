# Generated by Django 4.2 on 2023-04-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='pastebin_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='server',
            name='wrapper_ip',
            field=models.CharField(default='0.0.0.0', max_length=15),
        ),
        migrations.AddField(
            model_name='server',
            name='wrapper_port',
            field=models.CharField(default='443', max_length=5),
        ),
    ]
