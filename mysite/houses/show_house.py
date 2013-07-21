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
            help='Specify Owner to show'),
        )
        
    def handle(self, *args, **options):
        '''
        '''
        if options['owner']:
            try:
                h = House.objects.filter(owner=Owner.objects.filter(name=options['owner']))
                for i,val in enumerate(h):
                    self.stdout.write('id=[%s] Address=[%s]' % (h[i].id, h[i].address, endswith='')) 
                    for num in range(0, len(h[i].owner)):
                        self.stdout.write('Owner=[%s]' % h[i].owner.name)
                
            except Owner.DoesNotExist:
                self.stdout.write('Specified Owner=[%s] does not exist in the dataset'  % options['owner'])
        else:
            h = House.objects.all()
            for i,val in enumerate(h):
                self.stdout.write('id=[%s] Address=[%s]' % (h[i].id, h[i].address, endswith=''))
                    for num in range(0, len(h[i].owner)):
                        self.stdout.write('Owner=[%s]' % h[i].owner.name)