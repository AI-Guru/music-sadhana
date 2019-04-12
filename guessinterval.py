import librosa
import random
import getch
import time
import numpy as np
import utils

# Pitches to be used. One octave.
pitches = list(range(45, 45+12))

# Intervals to be used. One octave.
intervals = list(range(13))

# Play the game.
right_choices = 0
wrong_choices = 0
times = []
while True:
    first_pitch = random.choice(pitches)
    random_interval = random.choice(intervals)
    second_pitch = first_pitch + random_interval

    notes = [first_pitch, second_pitch]
    notes = [librosa.core.midi_to_note(note) for note in notes]

    print("Which interval is {}?".format(" - ".join(notes)))

    start_time = time.time()
    user_string = input()
    if user_string == "q":
        break

    if str(random_interval) == user_string:
        right_choices += 1
        print("Correct!")
    else:
        wrong_choices += 1
        print("Wrong! Expected: {}".format(random_interval))

    times.append(time.time() - start_time)
    time.sleep(1.0)

# Print results.
accuracy = int(100.0 * right_choices / (right_choices + wrong_choices))
average_time = np.mean(times)
print("Right: {} Wrong: {} Accuracy: {}% Average time: {}s".format(right_choices, wrong_choices, accuracy, average_time))

# Write results to statistics file.
values = [right_choices, wrong_choices, accuracy, average_time]
utils.append_values_to_csv(values, "intervals.txt")
