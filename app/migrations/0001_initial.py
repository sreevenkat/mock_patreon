# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-18 17:28
from __future__ import unicode_literals

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
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('benifit_type', models.CharField(blank=True, max_length=512, null=True)),
                ('rule_type', models.CharField(blank=True, choices=[('eom_monthly', 'eom_monthly'), ('one_time_immediate', 'one_time_immediate')], max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivered_delivarbles_count', models.IntegerField(default=0)),
                ('not_delivered_deliverables_count', models.IntegerField(default=0)),
                ('deliverables_due_today_count', models.IntegerField(default=0)),
                ('next_deliverable_due_date', models.DateTimeField(blank=True, null=True)),
                ('tiers_count', models.IntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('app_external_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('app_meta', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True, null=True)),
                ('creation_name', models.CharField(blank=True, max_length=256, null=True)),
                ('pay_per_name', models.CharField(blank=True, max_length=256, null=True)),
                ('one_liner', models.CharField(blank=True, max_length=512, null=True)),
                ('main_video_embed', models.URLField(blank=True, max_length=2048, null=True)),
                ('main_video_url', models.URLField(blank=True, max_length=2048, null=True)),
                ('image_url', models.URLField(blank=True, max_length=2048, null=True)),
                ('image_small_url', models.URLField(blank=True, max_length=2048, null=True)),
                ('thanks_video_url', models.URLField(blank=True, max_length=2048, null=True)),
                ('thanks_embed', models.URLField(blank=True, max_length=2048, null=True)),
                ('thanks_message', models.TextField(blank=True, max_length=2048, null=True)),
                ('is_monthly', models.BooleanField(default=False)),
                ('has_rss', models.BooleanField(default=False)),
                ('has_sent_rss_notify', models.BooleanField(default=False)),
                ('rss_feed_title', models.CharField(blank=True, max_length=1024, null=True)),
                ('rss_artwork_url', models.URLField(blank=True, max_length=2048, null=True)),
                ('is_nsfw', models.BooleanField(default=False)),
                ('is_charged_immediately', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pledge_url', models.URLField(blank=True, max_length=2048, null=True)),
                ('patron_count', models.IntegerField(blank=True, null=True)),
                ('discord_server_id', models.CharField(blank=True, max_length=512, null=True)),
                ('google_analytics_id', models.CharField(blank=True, max_length=512, null=True)),
                ('earnings_visibility', models.CharField(blank=True, choices=[('private', 'private'), ('public', 'public'), ('patrons_only', 'patrons_only')], max_length=100, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patron_status', models.CharField(blank=True, choices=[('active_patron', 'active_patron'), ('declined_patron', 'declined_patron'), ('former_patron', 'former_patron')], max_length=256, null=True)),
                ('is_follower', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('pledge_relationship_start', models.DateTimeField(blank=True, null=True)),
                ('lifetime_support_cents', models.IntegerField(default=0)),
                ('currently_entitled_amount_cents', models.IntegerField()),
                ('last_charge_date', models.DateTimeField(blank=True, null=True)),
                ('last_charge_status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Declined', 'Declined'), ('Deleted', 'Deleted'), ('Pending', 'Pending'), ('Refunded', 'Refunded'), ('Fraud', 'Fraud'), ('Other', 'Other')], max_length=128, null=True)),
                ('note', models.TextField()),
                ('will_pay_amount_cents', models.IntegerField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_cents', models.IntegerField(default=0, null=True)),
                ('user_limit', models.IntegerField(default=0, null=True)),
                ('remaining', models.IntegerField(default=0, null=True)),
                ('description', models.TextField()),
                ('requires_shipping', models.BooleanField(default=False)),
                ('url', models.URLField(max_length=2048, null=True)),
                ('patron_count', models.IntegerField(default=0)),
                ('post_count', models.IntegerField(default=0)),
                ('discord_role_ids', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=1024)),
                ('image_url', models.URLField(max_length=2048, null=True)),
                ('published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(null=True)),
                ('unpublished_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Campaign')),
            ],
        ),
        migrations.AddField(
            model_name='benefit',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Campaign'),
        ),
        migrations.AddField(
            model_name='benefit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
