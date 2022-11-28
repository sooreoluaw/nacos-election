from django.contrib import admin

from vote.models import Nominee, Poll, Voter

# Register your models here.
admin.site.register(Voter)
admin.site.register(Poll)
admin.site.register(Nominee)
