# Generated by Django 3.2.25 on 2024-06-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_uploadedvinrecord_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='goelectricrebates',
            name='notes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
