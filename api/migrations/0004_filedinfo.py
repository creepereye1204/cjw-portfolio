# Generated by Django 5.1.1 on 2024-11-23 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_skillset_badge_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiledInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filed', models.CharField(blank=True, max_length=30, null=True)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.skillset')),
            ],
            options={
                'verbose_name': 'Filed Info',
                'verbose_name_plural': 'Filed Infos',
            },
        ),
    ]
