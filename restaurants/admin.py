from django.contrib import admin
from .models import Restaurant, Waiter


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets =(
        ('Main Information', {
            'fields': ('name', 'description', 'count_of_employers', 'director', 'chef')
        }

        ),
        (
            'Contacts', {
                'fields': ('phone', 'country', 'city', 'street', 'house',)
            }
        ),
        ('Dishes', {
            'fields': ('serves_hot_dogs', 'serves_pizza', 'serves_sushi', 'serves_burgers',
                       'serves_donuts', 'serves_coffee')
        }
         )

    )


class WaiterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Biography', {'fields': ('restaurant',
                    'first_name',
                    'last_name',
                    'age',
                    'sex',)}),
    ('Contacts', {
    'fields': ('country',
    'city',
    'street',
    'house',
    'apartment',)}
    ),
    ('Education', {'fields':('seniority',
        'education',
        'courses',)})
    )


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)
