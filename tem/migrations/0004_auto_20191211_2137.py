# Generated by Django 2.2.5 on 2019-12-11 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tem', '0003_auto_20191211_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copomapp',
            name='id',
        ),
        migrations.AlterField(
            model_name='copomapp',
            name='CO_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tem.CO'),
        ),
    ]