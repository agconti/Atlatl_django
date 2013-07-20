from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from houses.models import Owner

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--name',
            action='store',
            type = 'string',
            dest='name',
            default=False,
            help='Add Owner to owner Model'),
        )

    def handle(self, *args, **options):
        if options['name']:
            try:
                o = Owner(name=options['name'])
                o.save()
            except Owner.unique_error_message:
                raise CommandError('Owner "%s" already exists' % options['name'])
    
            self.stdout.write('Successfully Added Owner Name="%s"' % options['name'])