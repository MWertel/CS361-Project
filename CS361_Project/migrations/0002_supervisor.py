# Generated by Django 4.1.2 on 2022-11-18 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CS361_Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CS361_Project.account')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
            ],
        ),
    ]
