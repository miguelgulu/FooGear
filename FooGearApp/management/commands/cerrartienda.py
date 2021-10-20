from django.core.management.base import BaseCommand, CommandError
from FooGearApp.models import Tienda

class CierraTienda(BaseCommand):
    help = 'Selecciona la tienda que quieras cerrar'

    def add_arguments(self, parser):
        parser.add_argument('Tienda_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for Tienda_id in options['Tienda_ids']:
            try:
                Tienda = Tienda.objects.get(pk=Tienda_id)
            except Tienda.DoesNotExist:
                raise CommandError('No existe la tienda "%s"' % Tienda_id)

            Tienda.opened = False
            Tienda.save()

            self.stdout.write(self.style.SUCCESS('Tienda "%s" cerrada con éxito' % Tienda_id))