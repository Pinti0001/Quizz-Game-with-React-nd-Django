# Generated by Django 3.2.4 on 2021-06-23 05:28


from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, default='photo.png', null=True, upload_to='photos/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=1000)),
            ],
        ),
    ]
