# Generated by Django 4.2.6 on 2023-10-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existencias',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.TextField(max_length=50),
        ),
    ]
