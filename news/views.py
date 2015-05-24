# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from feincms.views.decorators import standalone
from models import Person


def person_list(request):
    object_list = Person.objects.filter(active__exact=True).order_by('sort_order')
    context = RequestContext(request, {
        'object_list': object_list,
    })
    return render_to_response('team/person_list.html', {}, context_instance=context)


@standalone
def person_detail(request, person_nick_name):
    object = Person.objects.get(nick_name=person_nick_name)
    context = RequestContext(request, {
        'object': object,
    })
    return render_to_response('team/person_detail.html', {}, context_instance=context)
