from django.contrib import admin

from apps.contacts.models import ContactsBanner,ContactsInfo


admin.site.register(ContactsBanner)
admin.site.register(ContactsInfo)