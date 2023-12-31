from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter

# Register your models here.
from location.models import Country, City
from place.admin import PlaceMixinInline


class CityInline(admin.TabularInline):
    model = City
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]

    list_display = ['country_name']
    search_fields = ['country_name']
    list_filter = ['country_name']

    def has_change_permission(self, request, obj=None):
        return request.user.is_editor

    def has_delete_permission(self, request, obj=None):
        return request.user.is_deleter

class CountryFilter(admin.SimpleListFilter):
    title = 'Country'
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        countries = Country.objects.all()
        return [(country.id, country.country_name) for country in countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(country__id=self.value())
        else:
            return queryset


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ['city_name', 'country']
    search_fields = ['city_name', 'country__country_name']
    list_filter = [CountryFilter]

    def country(self, obj):
        return obj.country.country_name

    country.admin_order_field = 'country'

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            # Return empty list when creating a new city
            return []
        return super().get_inline_instances(request, obj)

    def has_change_permission(self, request, obj=None):
        return request.user.is_editor

    def has_delete_permission(self, request, obj=None):
        return request.user.is_deleter
