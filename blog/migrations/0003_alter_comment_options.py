# Generated by Django 3.2.15 on 2022-09-05 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-published_date']},
        ),
    ]
