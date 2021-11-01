# Generated by Django 3.2.8 on 2021-10-27 17:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('office', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
