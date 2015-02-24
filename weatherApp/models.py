from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.



class Location(models.Model):
	name = models.CharField(_("name"), max_length=255)
	location_id = models.CharField(
		_("Location ID"),
		max_length=255,
		help_text=_("Location IDs can be retrieved from URLs of weather "
            "at specific cities at Yahoo! Weather, e.g. GMXX0008 from "
            "http://weather.yahoo.com/forecast/GMXX0008.html"),
        )



	class Meta:

		verbose_name = _("Location")
		verbose_name_plural = _("Locations")




	def __unicode__(self):
		return self.name








class WeatherLog(models.Model):
    location = models.ForeignKey(Location, verbose_name=_("location"))
    timestamp = models.DateTimeField(_("timestamp"))
    temperature = models.IntegerField(_("temperature (C)"))
    humidity = models.IntegerField(_("humidity (%)"))
    wind_speed = models.DecimalField(
         _("wind speed (kmh)"),
         max_digits=5,
         decimal_places=2,
         )
    visibility = models.DecimalField(
         _("visibility (km)"),
         max_digits=5,
         decimal_places=2,
         )
    

    class Meta:

        verbose_name=_("weather log")
        verbose_name_plural=_("weather logs")
        ordering = ("-timestamp",)
    


    def __unicode__(self):
        return "%s @ %s" % (
            self.location.name,
            self.timestamp.strftime("%Y-%m-%dT%H:%M"),
            )







