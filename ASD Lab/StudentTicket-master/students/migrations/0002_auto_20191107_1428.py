# Generated by Django 2.2.6 on 2019-11-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
