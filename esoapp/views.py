from esoapp.models import Poll, Choice

from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'esoapp/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('esoapp:results', args=(p.id,)))