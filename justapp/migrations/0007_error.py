# Generated by Django 3.1.5 on 2021-01-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justapp', '0006_remove_urltimer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
