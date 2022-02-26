from mido import MidiFile

mid = MidiFile('examples/midi')

now = 0
for msg in mid:
    now = now + msg.time
    if msg.type == 'note_on' and msg.channel == 0:
        print(now, msg)




