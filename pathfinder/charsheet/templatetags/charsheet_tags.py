from django import template

register = template.Library()


@register.simple_tag
def skill(character, skill):
    return character.skill_bonus(skill)


@register.simple_tag
def trained(character, skill):
    return character.trained(skill)
