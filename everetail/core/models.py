from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from geoposition.fields import GeopositionField


class Address(models.Model):
	street = models.CharField(_("Street Name"), max_length=10, blank=True)
	city = models.CharField(_("City"), max_length=10, blank=True)
	state = models.CharField(_("State"), max_length=10, blank=True)
	country = models.CharField(_("Country"), max_length=10, blank=True)

	def __unicode__(self):
		return "{street}, {city} in {country} ".format(
            street=self.street, city=self.city, country=self.country)


class Outlet(TimeStampedModel):
	name = models.CharField(_('name'), max_length=100)
	slug = AutoSlugField(_('slug'), populate_from='name', unique=True)
	address = models.ForeignKey(Address, related_name='address')
	position = GeopositionField()


#==============================================================================
# SIGNALS
#==============================================================================
def get_geolocation(sender, instance, **kwargs):
    """
    A signal for hooking up automatic ``Geo Position`` creation.
    """
    print settings.MAPQUEST_KEY
    
models.signals.post_save.connect(get_geolocation, sender=Outlet)