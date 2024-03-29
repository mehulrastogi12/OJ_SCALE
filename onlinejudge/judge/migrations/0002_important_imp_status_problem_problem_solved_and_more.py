# Generated by Django 4.0.6 on 2022-07-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='important',
            name='Imp_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='problem',
            name='problem_solved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissions',
            name='lang',
            field=models.CharField(choices=[('C', 'GNU C'), ('CPP', 'GNU C++')], default='C', max_length=4),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_name',
            field=models.CharField(max_length=100),
        ),
    ]
