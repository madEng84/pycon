# Generated by Django 2.2.8 on 2020-01-17 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0009_remove_ranksubmission_topic_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='votes', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
