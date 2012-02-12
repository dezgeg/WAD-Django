from django.db import models

class Huone(models.Model):
	kapasiteetti = models.IntegerField()
	kerros = models.IntegerField()

	def __unicode__(self):
		return "Huone %d: kerros %d, %d/%d henkiloa" % (self.id, self.kerros,
				self.henkilot.count(), self.kapasiteetti)

class Henkilo(models.Model):
	nimi = models.CharField(max_length=30)
	puhelinnumero = models.CharField(max_length=10)
	osoite = models.CharField(max_length=100)
	huone = models.ForeignKey(Huone, null=True, related_name='henkilot')

	def __unicode__(self):
		return "%d: %s, osoite %s, puh. %s" % (self.id, self.nimi, self.osoite, self.puhelinnumero)
