from django.contrib import admin

from .models import Exhibition, Painting, Author, Booking


class PaintingInline(admin.TabularInline):
    model = Painting
    extra = 0


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0


class ExhibitionAdmin(admin.ModelAdmin):
    inlines = [PaintingInline, BookingInline]
    list_display = ('name', 'opened_at', 'ticket_price')
    list_filter = ['opened_at']
    search_fields = ['name']


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'exhibition', 'year', 'description')
    search_fields = ['name']


class AuthorAdmin(admin.ModelAdmin):
    inlines = [PaintingInline]
    list_display = ('name', 'country')
    list_filter = ['country']
    search_fields = ['name']


class BookingAdmin(admin.ModelAdmin):
    list_display = ('code', 'exhibition', 'user', 'booked_at')
    list_filter = ['booked_at', 'exhibition', 'user']
    search_fields = ['code']


admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Booking, BookingAdmin)
