# Generated by Django 3.2.9 on 2022-02-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='prenom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='tel',
            field=models.IntegerField(null=True),
        ),
    ]
