from typing import Any, Dict

from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

from webserver.pathfinder.models import Character
from webserver.util.view_decorators import template_view


@require_GET
@template_view('pathfinder/character_sheet.html')
def character_sheet(*, character_id: int) -> Dict[str, Any]:
    # character = get_object_or_404(Character, pk=character_id)

    return {'character': Character()}
