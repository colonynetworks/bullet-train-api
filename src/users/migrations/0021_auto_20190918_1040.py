# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-18 10:40
from __future__ import unicode_literals

import logging

from django.db import migrations, models

logger = logging.getLogger(__name__)

forward_sql = 'INSERT INTO organisations_userorganisation (user_id, organisation_id, date_joined, "role") ' \
              'SELECT ffadminuser_id, organisation_id, NOW(), \'ADMIN\' ' \
              'FROM users_ffadminuser_organisations'

reverse_sql = 'INSERT INTO users_ffadminuser_organisations (ffadminuser_id, organisation_id) ' \
              'SELECT user_id, organisation_id' \
              'FROM organisations_userorganisation'


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0020_auto_20181128_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ffadminuser',
            name='organisations'
        ),
        migrations.AddField(
            model_name='ffadminuser',
            name='organisations',
            field=models.ManyToManyField(blank=True, related_name='users', through='organisations.UserOrganisation',
                                         to='organisations.Organisation'),
        ),
        migrations.RunSQL(sql=forward_sql, reverse_sql=reverse_sql),
    ]
