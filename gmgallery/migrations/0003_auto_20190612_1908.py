# Generated by Django 2.2.1 on 2019-06-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gmgallery', '0002_auto_20190612_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmgallery',
            name='image',
            field=models.ImageField(default='myphoto/None/No-img.jpg', upload_to='myphoto/'),
        ),
    ]