# Generated by Django 3.1.6 on 2022-01-07 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_datafleets'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhitelistedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('create_user', models.CharField(default='SYSTEM', max_length=130)),
                ('update_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('update_user', models.CharField(max_length=130, null=True)),
                ('user', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'whitelisted_users',
            },
        ),
    ]
