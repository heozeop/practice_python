# Generated by Django 4.0 on 2022-04-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todocategory_todo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todo.todocategory'),
        ),
    ]
