# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Campaign(models.Model):

    Campaign_Visibility_Choices = (
        ('private', 'private'),
        ('public', 'public'),
        ('patrons_only', 'patrons_only'),
    )

    creator = models.ForeignKey(settings.AUTH_USER_MODEL)

    summary = models.TextField(null=True, blank=True)
    creation_name = models.CharField(max_length=256, null=True, blank=True)
    pay_per_name = models.CharField(max_length=256, null=True, blank=True)
    one_liner = models.CharField(max_length=512, null=True, blank=True)

    main_video_embed = models.URLField(max_length=2048, null=True, blank=True)
    main_video_url = models.URLField(max_length=2048, null=True, blank=True)
    image_url = models.URLField(max_length=2048, null=True, blank=True)
    image_small_url = models.URLField(max_length=2048, null=True, blank=True)
    thanks_video_url = models.URLField(max_length=2048, null=True, blank=True)
    thanks_embed = models.URLField(max_length=2048, null=True, blank=True)
    thanks_message = models.TextField(max_length=2048, null=True, blank=True)

    is_monthly = models.BooleanField(default=False)
    has_rss = models.BooleanField(default=False)
    has_sent_rss_notify = models.BooleanField(default=False)

    rss_feed_title = models.CharField(max_length=1024, null=True, blank=True)
    rss_artwork_url = models.URLField(max_length=2048, null=True, blank=True)
    is_nsfw = models.BooleanField(default=False)
    is_charged_immediately = models.BooleanField(default=False)
    
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    pledge_url = models.URLField(max_length=2048, null=True, blank=True)
    patron_count = models.IntegerField(null=True, blank=True)
    discord_server_id = models.CharField(max_length=512, null=True, blank=True)
    google_analytics_id = models.CharField(max_length=512, null=True, blank=True)

    earnings_visibility = models.CharField(max_length=100, null=True, blank=True, choices=Campaign_Visibility_Choices)
    deleted = models.BooleanField(default=False)
    


class Tier(models.Model):

    campaign = models.ForeignKey('Campaign')
    amount_cents = models.IntegerField(default=0, null=True)
    user_limit = models.IntegerField(default=0, null=True)
    remaining = models.IntegerField(default=0, null=True)
    description = models.TextField()
    requires_shipping = models.BooleanField(default=False)
    url = models.URLField(max_length=2048, null=True)
    patron_count = models.IntegerField(default=0)
    post_count = models.IntegerField(default=0)
    discord_role_ids = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=1024)
    image_url = models.URLField(max_length=2048, null=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    unpublished_at = models.DateTimeField(null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

class Member(models.Model):

    Patron_Status_Choices = (
        ('active_patron', 'active_patron'),
        ('declined_patron', 'declined_patron'),
        ('former_patron', 'former_patron'),
    )

    Charge_Choices_Status = (
        ('Paid', 'Paid'),
        ('Declined', 'Declined'),
        ('Deleted', 'Deleted'),
        ('Pending', 'Pending'),
        ('Refunded', 'Refunded'),
        ('Fraud', 'Fraud'),
        ('Other', 'Other'),
    )

    patron_status = models.CharField(max_length=256, null=True, 
                        blank=True, choices=Patron_Status_Choices)
    is_follower = models.BooleanField(default=False)
    full_name = models.CharField(max_length=256)
    email = models.EmailField()
    pledge_relationship_start = models.DateTimeField(null=True, blank=True)
    lifetime_support_cents = models.IntegerField(default=0)
    currently_entitled_amount_cents = models.IntegerField()
    last_charge_date = models.DateTimeField(null=True, blank=True)
    last_charge_status = models.CharField(max_length=128, null=True, 
                            blank=True, choices=Charge_Choices_Status)
    note = models.TextField()
    will_pay_amount_cents = models.IntegerField()
