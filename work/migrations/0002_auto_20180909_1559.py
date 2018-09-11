# Generated by Django 2.1.1 on 2018-09-09 22:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='title',
            new_name='employer',
        ),
        migrations.AddField(
            model_name='work',
            name='position',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='work',
            name='start_date',
            field=models.DateField(),
        ),
    ]
