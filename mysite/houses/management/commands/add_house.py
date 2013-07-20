from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from houses.models import House, Owner

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--owner',
            action='store',
            type = 'string',
            dest='owner',
            default=False,
            help='Add Owner to owner Model'),
        
        make_option('--address',
            action='store',
            type = 'string',
            dest='address',
            default=False,
            help='Add house address to house model'),
        )

    def handle(self, *args, **options):
        '''
        '''
        if (options['address'] != None) and (options['owner'] != None):
            try:
                o = Owner(name = options['owner'])
                o.save()
                o.house_set.create(address = options['address'])
                self.stdout.write('Successfully Added House: %s and Owner Name=%s'  % (options['address'], options['owner']))
                
            except Owner.unique_error_message:
                o = Owner.objects.filter(name='Luke Skywalker')
                o.house_set.create(address = options['address'])
                self.stdout.write('Successfully Added House: %s to Owner Name=%s'  % (options['address'], options['owner']))
        else:
            print 'Please include address AND owner!'