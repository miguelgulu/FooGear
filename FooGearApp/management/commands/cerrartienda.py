from django.core.management.base import BaseCommand, CommandError
from FooGearApp.models import Tienda

class Command(BaseCommand):
    help = 'Cierra la tienda especificada'

    def add_arguments(self, parser):
        parser.add_argument('tienda_ids', nargs='+', type=int)


    def handle(self, *args, **options):
        for tienda_id in options['tienda_ids']:
            try:
                tienda = Tienda.objects.get(pk=tienda_id)
            except Tienda.DoesNotExist:
                raise CommandError('Tienda "%s" no existe' % tienda_id)

            tienda.delete()


            self.stdout.write(self.style.SUCCESS('Cerrada con éxito la tienda "%s"' % tienda_id))