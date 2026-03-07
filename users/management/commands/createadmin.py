from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email = "admin@mail.ru",
            first_name = "Admin",
            last_name = "Admine"
        )
        user.set_password('asd1234zxc')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS("'Admin' успешно создан!"))
