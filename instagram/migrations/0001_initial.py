# Generated by Django 3.0.4 on 2020-03-11 07:55

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import instagram.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('bio', tinymce.models.HTMLField()),
                ('profile_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, instagram.models.CrudMethods),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_caption', tinymce.models.HTMLField()),
                ('post_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile')),
            ],
            bases=(models.Model, instagram.models.CrudMethods),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile')),
            ],
            bases=(models.Model, instagram.models.CrudMethods),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='instagram.Profile')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='instagram.Profile')),
            ],
            bases=(models.Model, instagram.models.CrudMethods),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', tinymce.models.HTMLField()),
                ('comment_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Post')),
                ('comment_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, instagram.models.CrudMethods),
        ),
    ]
