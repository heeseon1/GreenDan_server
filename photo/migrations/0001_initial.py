# Generated by Django 4.2.3 on 2023-07-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='photos/')),
                ('name', models.CharField(max_length=60)),
                ('ai_name', models.CharField(blank=True, max_length=60, null=True)),
                ('state', models.CharField(blank=True, choices=[('GOOD', 'normal'), ('BAD', 'complaint'), ('ETC', 'etc')], default='GOOD', max_length=20, null=True)),
                ('explain', models.CharField(blank=True, max_length=60, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 일시')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'ordering': ['-created_at'],
            },
        ),
    ]
