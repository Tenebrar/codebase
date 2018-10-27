import wave

from hacker.settings import inputfile, outputfile

# satan.mp3 was converted to satan.wav using:
# http://audio.online-convert.com/convert-to-wav

with wave.open(inputfile('crypto', 'voices_in_my_head', 'satan.wav'), 'r') as w, \
        wave.open(outputfile('crypto', 'voices_in_my_head', 'satan_rev.wav'), 'w') as w_reversed:
    w_reversed.setparams(w.getparams())

    length = w.getnframes()
    frames = [w.readframes(1) for _ in range(length)]

    for frame in frames[::-1]:
        w_reversed.writeframes(frame)

# The file then says
print('The answer is insecticide')
