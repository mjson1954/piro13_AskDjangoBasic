from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
import logging

logger = logging.getLogger(__name__)

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year))


def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs.filter(name__icontains=q)
    logger.debug('query: {}'.format(q))
    return render(request, 'shop/itme_list.html',{
        'item_list': qs,
    })