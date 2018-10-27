from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from charsheet.models import Character, Roll, Skill
from util.decorators import template_view


@template_view('charsheet/index.html')
def index():
    # For now, shows everything. Should the amount become too large, this should change
    characters = Character.objects.order_by('name')
    return {'characters': characters}


@template_view('charsheet/sheet.html')
def sheet(character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    skills = Skill.objects.all()
    return {'character': character, 'skills': skills}


@template_view('charsheet/detail.html')
def detail(character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    skills = Skill.objects.all()
    return {'character': character, 'skills': skills}


def add_roll(request: HttpRequest, character_id: int) -> HttpResponse:
    reason = request.POST['reason']
    die_size = request.POST['die_size']
    result = request.POST['result']

    assert die_size <= result  # This can be done front-end as well (Django form validation)

    roll = Roll(die_size=die_size, result=result, reason=reason, character_id=character_id)
    roll.save()

    return HttpResponseRedirect(reverse('charsheet:detail', args=(character_id,)))

# Not sure yet of other views, apply enlarge, apply spell,...
