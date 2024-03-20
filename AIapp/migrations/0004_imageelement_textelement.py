# Generated by Django 4.0 on 2024-03-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIapp', '0003_alter_imageai_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='mediaphoto')),
            ],
        ),
        migrations.CreateModel(
            name='TextElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
