# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 11:13


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'mailgun_attachments/', verbose_name='file')),
                ('content_id', models.CharField(blank=True, help_text='Content-ID (CID) referencing this attachment.', max_length=255, verbose_name='Content-ID')),
            ],
            options={
                'verbose_name': 'attachment',
                'verbose_name_plural': 'attachments',
            },
        ),
        migrations.CreateModel(
            name='IncomingEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=255, verbose_name='sender')),
                ('from_str', models.CharField(max_length=255, verbose_name='from')),
                ('recipient', models.CharField(max_length=255, verbose_name='recipient')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('body_plain', models.TextField(blank=True, verbose_name='body plain')),
                ('body_html', models.TextField(blank=True, verbose_name='body html')),
                ('stripped_text', models.TextField(blank=True, verbose_name='stripped text')),
                ('stripped_html', models.TextField(blank=True, verbose_name='stripped html')),
                ('stripped_signature', models.TextField(blank=True, verbose_name='stripped signature')),
                ('message_headers', models.TextField(blank=True, help_text='Stored in JSON.', verbose_name='message headers')),
                ('content_id_map', models.TextField(blank=True, help_text='Dictionary mapping Content-ID (CID) values to corresponding attachments. Stored in JSON.', verbose_name='Content-ID map')),
                ('received', models.DateTimeField(auto_now_add=True, verbose_name='received')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'incoming email',
                'verbose_name_plural': 'incoming emails',
            },
        ),
        migrations.AddField(
            model_name='attachment',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailgun_incoming.IncomingEmail', verbose_name='email'),
        ),
    ]
