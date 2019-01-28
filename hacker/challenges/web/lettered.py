from html.entities import html5

value = '&#38&#119&#101&#105&#101&#114&#112&#59&#38&#79&#116&#105&#108&#100&#101&#59&#38&#85&#103&#114&#97&#118&#101&#59&#38&#114&#101&#97&#108&#59&#38&#99&#111&#112&#121&#59&#38&#84&#104&#101&#116&#97&#59&#38&#102&#110&#111&#102&#59&#38&#102&#110&#111&#102&#59&#38&#105&#115&#105&#110&#59&#38&#105&#115&#105&#110&#59'  # noqa

value = ''.join(map(chr, map(int, value.split('&#')[1:])))
value = ''.join(map(lambda x: html5.get(x, 'X'), value[1:].split('&')))

print(value)  # Then, visually you will see it spells 'pourcoffee', I don't think programmatic conversion is realistic
