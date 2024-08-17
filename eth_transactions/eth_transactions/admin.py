from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['txhash', 'blockno', 'from_address', 'to_address', 'value_in_eth', 'datetime_utc']
    search_fields = ['txhash', 'from_address', 'to_address']
    list_filter = ['blockno', 'datetime_utc']
