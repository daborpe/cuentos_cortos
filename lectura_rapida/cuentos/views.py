# coding: utf-8
from annoying.decorators import render_to
from .models import Cuento


@render_to('test.html')
def test(request):
    cuentos = Cuento.objects.filter(active=True).order_by('?')[:1]
    return {'cuentos': cuentos}
