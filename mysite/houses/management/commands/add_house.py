from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
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
                # to add house and owner
                o,create_owner = Owner.objects.get_or_create(name = options['owner'])
                
                # if an owner was created sync the database
                #if (create_owner == True):
                #    import subprocess
                #    subprocess.Popen(["python", "manage.py", "syncdb"])
                
                # create / get the house 
                o,create_house_owner = House.objects.get_or_create(address=options['address'], owner=(o))
                
                if create_owner == True:
                    self.stdout.write(
                                      'Successfully Added House: %s and Owner=%s'  
                                      % (options['address'], options['owner'])
                                      )
                
                elif create_house_owner == True: 
                    self.stdout.write(
                                      'Successfully Added House: %s to Owner=%s'  
                                      % (options['address'], options['owner'])
                                      )
                else:
                    self.stdout.write('method failed to create an owner or a house')
                    
            except IntegrityError:
                self.stdout.write('There is already a house associated with that Owner')
        else:
            print 'Please include address AND owner!'