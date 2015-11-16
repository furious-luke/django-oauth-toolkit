# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from oauth2_provider.settings import oauth2_settings
from django.db import models, migrations
import oauth2_provider.validators
import oauth2_provider.generators
from django.conf import settings


class ConditionallyAddField(migrations.AddField):

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if getattr(settings, 'ADD_SKIP_AUTHORIZATION_FIELD', True):
            super(ConditionallyAddField, self).database_forwards(app_label, schema_editor, from_state, to_state)


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0001_initial'),
    ]

    operations = [
        ConditionallyAddField(
             model_name='Application',
             name='skip_authorization',
             field=models.BooleanField(default=False),
             preserve_default=True,
        ),
        migrations.AlterField(
            model_name='Application',
            name='user',
            field=models.ForeignKey(related_name='oauth2_provider_application', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='AccessToken',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
