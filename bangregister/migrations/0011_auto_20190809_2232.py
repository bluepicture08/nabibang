# Generated by Django 2.1.8 on 2019-08-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangregister', '0010_auto_20190809_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangregister.Room'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangregister.Room'),
        ),
    ]
