# Generated by Django 3.1.5 on 2021-09-18 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_type', models.CharField(blank=True, max_length=200, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=400, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=400, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='skill_and_sallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.offer')),
            ],
        ),
    ]
