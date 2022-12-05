# Generated by Django 4.1.3 on 2022-12-05 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CS361_Project', '0002_supervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('departament', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LabSection',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('departament', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='telephone',
        ),
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='telephone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='supervisorAccount',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CS361_Project.account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TAAccount', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CS361_Project.account')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CS361_Project.course')),
                ('labSection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CS361_Project.labsection')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CS361_Project.course')),
                ('instructorAccount', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CS361_Project.account')),
                ('labSection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CS361_Project.labsection')),
            ],
        ),
    ]