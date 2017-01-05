from django.db import models

class SpeciesChiroptera(models.Model):
    """ """
    taxonid = models.CharField(max_length=30)
    order_name = models.CharField(max_length=120)
    family_name = models.CharField(max_length=120)
    genus_name = models.CharField(max_length=120)
    scientific_name = models.CharField(max_length=120)
    population = models.CharField(max_length=1000)
    category_global = models.CharField(max_length=30) # Source: category.

class Countries(models.Model):
    """ """
    country_isocode = models.CharField(max_length=30) # Source: isocode.
    country_name = models.CharField(max_length=120) # Source: country.

class ChiropteraByCountry(models.Model):
    """ """
    country_isocode = models.CharField(max_length=30) # Source: country.
    taxonid = models.CharField(max_length=30)
    category_country = models.CharField(max_length=30) # Source: category.

