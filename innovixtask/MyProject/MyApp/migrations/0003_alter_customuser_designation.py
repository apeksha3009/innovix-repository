# Generated by Django 4.1.5 on 2023-01-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0002_alter_customuser_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="designation",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
