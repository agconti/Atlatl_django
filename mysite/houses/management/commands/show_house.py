from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.forms.models import model_to_dict
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
        #get fields for house model
        fields = House.objects.model._meta.fields
                
        if options['owner']:
            try:
                #get houses for owner
                house_querry = House.objects.filter(owner=Owner.objects.filter(name=options['owner']))
                #print houses for owner to console
                for i,val in enumerate(house_querry):
                    for f in fields:
                        self.stdout.write('%s=[%s],' % (f.attname,f.value_from_object(house_querry[i])), ending='')
                    self.stdout.write('')
            except Owner.DoesNotExist:
                self.stdout.write('Specified Owner=[%s] does not exist in the dataset'  % options['owner'])
        else:
            #get all houses
            house_querry = House.objects.all()
            #print all houses to console
            for i,val in enumerate(house_querry):
                for f in fields:
                    self.stdout.write('%s=[%s],' % (f.attname,f.value_from_object(house_querry[i])), ending='')
                self.stdout.write('')