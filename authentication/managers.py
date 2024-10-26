from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, rut, correo_electronico, password, **extra_fields):
        if not rut:
            raise ValueError(_("Debe ingresar un rut"))
        if not correo_electronico:
            raise ValueError(_("Debe ingresar un correo electrónico"))
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(rut=rut, correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, rut, correo_electronico, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("rol", 'ADMINISTRADOR')

        return self.create_user(rut, correo_electronico, password, **extra_fields)
