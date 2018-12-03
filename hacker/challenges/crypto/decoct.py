value = '11114604011104087145821450408415704084145154154040911578504084150141840408415015183040871418304014115604014514614615114315114515684040145156143157144151156147040831431501451551450540408715785154144040911578504014214515415114586145040155145077040131157858204014115683871458204015183040047838482157808091047056'  # noqa

index = 0
result = ''
while index < len(value):
    sub = value[index:index + 3]
    try:
        c = chr(int(sub, 8))
    except ValueError:
        sub = value[index:index + 2]
        c = chr(int(sub)).lower()  # Lower is for readability, these characters seem unnecessarily encoded as capitals

    result += c
    index += len(sub)

print(result)  # This contains a mistake, but it is not caused by the decoding
print(result.replace('[', 'y'))  # The replace is obvious from the rest of the deciphered text
