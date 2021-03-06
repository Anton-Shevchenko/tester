# Generated by Django 2.2.1 on 2020-05-10 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('task_id', models.IntegerField()),
                ('status', models.IntegerField()),
                ('assessment', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('params', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('params', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Group')),
            ],
        ),
    ]
