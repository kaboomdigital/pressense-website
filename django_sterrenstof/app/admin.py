from django.contrib import admin
from .models import Programma, FestivalInfo, FooterInfo


# class ProjectDetailInline(admin.TabularInline):
#     model = ProjectDetail
#     extra = 0
#     ordering = ('-project', 'table_row_number', )
#
#
# class ProjectImagesInline(admin.TabularInline):
#     model = ProjectImages
#     extra = 0
#     ordering = ('-project', 'order_id',)


class ProgrammaAdmin(admin.ModelAdmin):
    # inlines = [ProjectDetailInline, ProjectImagesInline]
    search_fields = ['naam', ]
    # save_as = True
    list_display = ('naam', 'tijd_slot', 'locatie', 'font_size', 'link_kleur', 'weergave_volgorde', 'geactiveerd',)
    list_editable = ('tijd_slot', 'locatie', 'font_size', 'link_kleur', 'weergave_volgorde', 'geactiveerd',)
    # list_filter = ('geactiveerd', 'link_kleur', )
    ordering = ('weergave_volgorde',)
    fieldsets = (
        ('Programma item', {
            'fields':
                (('naam', 'url'), 'omschrijving', ('tijd_slot', 'locatie'), ('afbeelding', 'thumbnail'), ),
            'description':
                (
                    'Zorg voor een duidelijke url.'),
        }),
        ('Item styling', {
            'fields':
                (('font_size', 'link_kleur'),),
            'description':
                (
                    'Kies de styling voor de links op de programma overzicht pagina'),
        }),
        ('Item dispay', {
            'fields':
                ('weergave_volgorde', 'geactiveerd',),
            'description':
                (
                    'De weergave volgorde is belangrijk voor de werking van de pijltjes navigatie!'),
        }),
    )


class FestivalInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Wijzig de Festival Info pagina', {
            'fields':
                ('content',),
        }),
    )


class FooterInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact info', {
            'fields':
                ('header', 'locatie', 'contact'),
            'description':
                (
                    'De styling van de webpagina zorgt ervoor dat de teksten automatisch in hoofdletters worden weergegeven. Ik raad aan hier dus gewoon hoofdletters te gebruiken volgens onze taal-regels.'),
        }),
        ('Tickets', {
            'fields':
                (('ticket_early', 'ticket_regular', 'ticket_kids', 'ticket_cjp'),)
        }),
        ('Social-links', {
            'fields':
                ('facebook_url', 'instagram_url'),
        }),
    )


# Register your models here.
admin.site.register(Programma, ProgrammaAdmin)
admin.site.register(FestivalInfo, FestivalInfoAdmin)
admin.site.register(FooterInfo, FooterInfoAdmin)

admin.site.site_header = 'Sterrenstof administration'
