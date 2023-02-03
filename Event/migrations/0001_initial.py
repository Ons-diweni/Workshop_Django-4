# Generated by Django 4.1.6 on 2023-02-02 23:58

import Event.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(verbose_name='description')),
                ('evt_date', models.DateField(validators=[Event.models.dateValidator])),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('state', models.BooleanField(default=False)),
                ('nbe_participant', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='This value should be greater than or equal to zero')])),
                ('Category', models.CharField(choices=[('Music', 'Music'), ('Cinema', 'Cinema'), ('Sport', 'Sport')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
