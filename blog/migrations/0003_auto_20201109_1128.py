# Generated by Django 2.2.17 on 2020-11-09 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_item_todolist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='user',
        ),
        migrations.DeleteModel(
            name='item',
        ),
        migrations.DeleteModel(
            name='ToDolist',
        ),
    ]
