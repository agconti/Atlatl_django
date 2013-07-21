from optparse import make_option
from exceptions import IndexError
from django.core.management.base import BaseCommand, CommandError
from houses.models import House, Owner

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--addr-contains',
            action='store',
            type = 'string',
            dest='addr',
            default=False,
            help='Specify Owner to show'),
        )
        
    def handle(self, *args, **options):
        '''
        '''
        if options['addr']:
            # delete house
            try:
                #setup owner list 
                house_owners = []
                # delete house
                h = House.objects.filter(address__contains=options['addr'])
                for i in h:
                    house_owners.append(i.owner)
                    i.delete()
                    self.stdout.write('House at [%s] was deleted' % i.address)
            except:
                self.stdout.write(
                                  'There is no house containing [%s] in the dataset'  
                                  % options['addr']
                                  )
            
            #delete owner
            try:
                for o in house_owners:
                    # check their # of houses
                    if len(House.objects.filter(owner=(o))) < 1:
                        o.delete()
                        self.stdout.write('Owner [%s] was deleted' % o.name )
            except IndexError:
                self.stdout.write('There was an Error deleting Owner [%s]' % o.name )