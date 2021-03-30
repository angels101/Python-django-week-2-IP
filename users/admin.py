# User models

# Django
from django.contrib.auth.models import User
from django.db import models

# User your models here.


class Profile(models.Model):
    """
    Profile model

    Proxy Model that extends the base data with other information.
    """
    # Relation of  user table
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Campos extendidos
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    # time
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    # Lista de los atributos que mostrara en el admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # Lista de links que llevan al detalle
    list_display_links = ('pk', 'user')
    # Lista de editables in situ
    list_editable = ('phone_number', 'website', 'picture')
    # Campos en los que se puede buscar
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # Campos por los que se puede filtrar
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    # Agrupar campos
    fieldsets = (
        (
            'Profile',
            {
                # Para organizarlos horizontalmente se puede hacer
                # colocando una tupla dentro de otra tupla y la coma
                # (('user', 'picture'),)
                'fields': (('user', 'picture'),)
            }
        ),
        # Si no queremos que aparezca
        # la barra azul de titulo podemos pasarle None
        (
            'Extra info',
            {
                'fields': (
                    ('phone_number', 'website'),
                    ('biography'),
                )
            }
        ),
        (
            'Metadata',
            {
                'fields': (('created', 'modified'),)
            }
        ),
    )
    readonly_fields = ('created', 'modified')

# Para que ambos admins se vean en uno solo se hace de la sgte forma


class ProfileInline(admin.StackedInline):
        """Profile in-line admin for users."""
        model = Profile
        can_delete = False
        verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
# admin.site.register(Modelo,Clase)
admin.site.register(User, UserAdmin)
_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username