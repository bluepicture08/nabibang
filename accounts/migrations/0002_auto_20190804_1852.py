# Generated by Django 2.2.4 on 2019-08-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', '여자'), ('male', '남자')], max_length=128),
        ),
    ]
