from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from products.models import RFID

class RFIDResource(ModelResource):
    class Meta:
        queryset = RFID.objects.all()
        # resource_name = 'p'
        #authorization = DjangoAuthorization()
        authorization = Authorization() #disable auth
        #authentication = BasicAuthentication()