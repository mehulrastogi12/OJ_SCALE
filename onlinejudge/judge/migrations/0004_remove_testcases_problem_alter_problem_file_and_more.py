# Generated by Django 4.0 on 2022-07-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_submissions_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcases',
            name='problem',
        ),
        migrations.AlterField(
            model_name='problem',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='Submissions',
        ),
        migrations.DeleteModel(
            name='Testcases',
        ),
    ]