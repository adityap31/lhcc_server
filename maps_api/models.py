from django.db import models


class Country(models.Model):
    """Model definition for Country."""

    name = models.CharField(max_length=30, unique=True, null=True, blank=True)

    class Meta:
        """Meta definition for Country."""

        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        """Unicode representation of Country."""
        return self.name


class City(models.Model):
    """Model definition for City."""

    name = models.CharField(max_length=30, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        """Meta definition for City."""

        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        """Unicode representation of City."""
        return self.name
