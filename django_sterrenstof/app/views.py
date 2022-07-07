from django.shortcuts import render
from next_prev import next_in_order, prev_in_order
from .models import Programma, FestivalInfo, FooterInfo

qs_footer = FooterInfo.objects.all()

# Create your views here.
def index(request):
    # programma = Programma.objects.filter(geactiveerd=True).order_by('weergave_volgorde')
    return render(request, 'app/index.html', {'domain': request.get_host(),
                                                 'url': request.build_absolute_uri(),
                                                 'footer_info': qs_footer
                                                 })


def programma(request):
    programma = Programma.objects.filter(geactiveerd=True).order_by('weergave_volgorde')
    return render(request, 'app/programma.html', {'programma': programma,
                                                     'domain': request.get_host(),
                                                     'url': request.build_absolute_uri(),
                                                     'footer_info': qs_footer
                                                     })


def programma_details(request, programma_url):
    programma = Programma.objects.filter(url=programma_url)

    qs = Programma.objects.filter(geactiveerd=True).order_by('weergave_volgorde')
    current = Programma.objects.get(url=programma_url)
    next = next_in_order(current, qs=qs)
    prev = prev_in_order(current, qs=qs)

    return render(request, 'app/programma_details.html', {'programma': programma,
                                                             'next': next,
                                                             'prev': prev,
                                                             'domain': request.get_host(),
                                                             'url': request.build_absolute_uri(),
                                                             'footer_info': qs_footer
                                                             })


def festival_info(request):
    qs = FestivalInfo.objects.all()
    return render(request, 'app/festival_info.html', {'festival_info': qs,
                                                         'domain': request.get_host(),
                                                         'url': request.build_absolute_uri(),
                                                         'footer_info': qs_footer
                                                         })


def time_table(request):
    return render(request, 'app/time_table.html', {'domain': request.get_host(),
                                                         'url': request.build_absolute_uri(),
                                                         'footer_info': qs_footer
                                                         })
