# Generated by Django 3.1.5 on 2021-09-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210918_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='img',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]