from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.utils.html import escape


def generate_filename_thumbnail(self, filename):
    url = "images/{}/thumbnail_{}__{}".format(self.url, self.url, filename)
    return url


def generate_filename(self, filename):
    """ Generate a filename for the project images upload field"""
    url = "images/{}/afbeelding_{}__{}".format(self.url, self.url, filename)
    return url


# Create your models here.
class Programma(models.Model):
    """ a model for the festival program """

    LINK_KLEUR_CHOICES = (
        ('programma__label--muziek', 'programma__label--muziek'),
        ('programma__label--sprekers', 'programma__label--sprekers'),
        ('programma__label--ook-leuk', 'programma__label--ook-leuk'),
        ('programma__label--kids', 'programma__label--kids'),
        ('programma__label--workshops', 'programma__label--workshops'),
        ('programma__label--food', 'programma__label--food'),
        ('programma__label--healing', 'programma__label--healing'),
        ('programma__label--km-area', 'programma__label--km-area')
    )

    url = models.SlugField(max_length=100, help_text="Vul de url voor het item in: <em>dit-is-een-voorbeeld-url</em>")
    naam = models.CharField(max_length=200)
    omschrijving = models.TextField(help_text=escape('Gebruik de volgende HTML-tag voor het begin van elke paragraaf <p class="paragraph"> en sluit elke paragraaf af met een </p> tag. Gekijk eventueel een reeds bestaand programma item voor referentie.'))

    afbeelding = ProcessedImageField(upload_to=generate_filename,
                                     processors=[ResizeToFit(1000, 1000, False)],
                                     format='JPEG',
                                     options={'quality': 60},
                                     help_text="Upload een 'grote' afbeelding voor op de programma item pagina")

    thumbnail = ProcessedImageField(upload_to=generate_filename_thumbnail,
                                    processors=[ResizeToFit(400, 400, False)],
                                    format='JPEG',
                                    options={'quality': 60},
                                    help_text="Upload een kleine afbeelding voor op het programma overzicht. Een afbeelding zo rond de 400x200px (max. 100Kb) is prima.")

    tijd_slot = models.CharField(max_length=16, help_text="Gebruik het volgende formaat: <em>1200 - 1400</em>.")
    locatie = models.CharField(max_length=40)
    font_size = models.DecimalField(verbose_name='Lettertype grootte (in Em)', default=1, max_digits=5, decimal_places=2, help_text="Bepaal het tekst-formaat van de link op het programma overzicht")
    link_kleur = models.CharField(max_length=40, choices=LINK_KLEUR_CHOICES, default='programma__label--muziek', help_text="Kies een kleur voor de link op het programma overzicht")
    weergave_volgorde = models.PositiveSmallIntegerField(verbose_name='Weergave Volgorde', default=1, help_text="Hoe hoger hoe meer links-boven, hoe lager hoe meer rechts-onder")
    geactiveerd = models.BooleanField(default=False, help_text="Bepaal of het programma-item zichtbaar is voor de website bezoeker")

    class Meta:
        verbose_name = 'Programma Item'
        verbose_name_plural = 'Programma Items'
        ordering = ('naam', )

    def __str__(self):
        return self.naam
        # return '{}, {}, {}'.format(self.project, 'Order ID: ' + str(self.order_id), self.image)


class FestivalInfo(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = 'Festival Info'
        verbose_name_plural = 'Festival Info'

    def __str__(self):
        return 'Festival Info'


class FooterInfo(models.Model):
    header = models.CharField(max_length=100)
    locatie = models.CharField(max_length=100)
    contact = models.EmailField(max_length=50)
    ticket_early = models.CharField(max_length=6)
    ticket_regular = models.CharField(max_length=6)
    ticket_kids = models.CharField(max_length=6)
    ticket_cjp = models.CharField(max_length=6)
    facebook_url = models.CharField(max_length=200)
    instagram_url = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Info'

    def __str__(self):
        return 'Footer Info'
