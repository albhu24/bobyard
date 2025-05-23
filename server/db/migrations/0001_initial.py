# Generated by Django 5.2 on 2025-04-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('likes', models.IntegerField()),
                ('image', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
