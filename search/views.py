import pdb

from django.shortcuts import render, redirect
from django.db.models import Q

from web.models import Note


def get_search(request):
    q_text = request.GET.get('q')

    notes = Note.objects.filter(user=request.user).filter(
        Q(title__contains=q_text) | Q(content__contains=q_text)
    )
    # pdb.set_trace()

    return render(request, 'search.html', {'notes': notes})