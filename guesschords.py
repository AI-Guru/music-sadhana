import librosa
import random
import getch
import time
import numpy as np

chords = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7]
}

pitches = list(range(45, 45+12))
notes = [librosa.core.midi_to_note(pitch) for pitch in pitches]

symbolic_chords = {}
for chord, offsets in chords.items():
    symbolic_chords[chord] = []
    for pitch in pitches:
        notes = []
        for offset in offsets:
            notes.append(pitch + offset)
        notes = [librosa.core.midi_to_note(note) for note in notes]
        notes = [''.join([i for i in note if not i.isdigit()]) for note in notes]
        notes = [str(note) for note in notes]
        symbolic_chord = "-".join(notes)
        symbolic_chords[chord].append(symbolic_chord)

right_choices = 0
wrong_choices = 0
times = []
while True:
    random_index = random.choice(list(range(len(list(symbolic_chords.keys())))))
    random_key = list(symbolic_chords.keys())[random_index]
    random_chord = random.choice(symbolic_chords[random_key])
    print()
    print("{}".format(random_chord), " " .join([" ({}) {}".format(index + 1, key) for index, key in enumerate(symbolic_chords.keys())]))
    expected_character = str(random_index + 1)

    start_time = time.time()
    character = getch.getch()
    if character == "q":
        break

    if expected_character == character:
        right_choices += 1
        print("Correct!")
    else:
        wrong_choices += 1
        print("Wrong!")

    times.append(time.time() - start_time)
    time.sleep(1.0)

accuracy = int(100.0 * right_choices / (right_choices + wrong_choices))
average_time = np.mean(times)
print("Right: {} Wrong: {} Accuracy: {}% Average time: {}s".format(right_choices, wrong_choices, accuracy, average_time))
