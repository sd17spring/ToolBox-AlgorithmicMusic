"""Synthesizes a blues solo algorithmically."""

import atexit
import os
from random import choice

from psonic import *

# The sample directory is relative to this source directory.
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "samples")

SAMPLE_FILE = os.path.join(SAMPLES_DIR, "bass_D2.wav")
SAMPLE_NOTE = D2


def play_note(note, beats=1, bpm=60, amp=1):
    """Plays note for `beats` beats. Returns when done."""
    # `note` is this many half-steps higher than the sampled note
    half_steps = note - SAMPLE_NOTE
    # An octave higher is twice the frequency. There are twelve half-steps per octave. Ergo,
    # each half step is a twelth root of 2 (in equal temperament).
    rate = (2 ** (1 / 12)) ** half_steps
    assert os.path.exists(SAMPLE_FILE)
    # Turn sample into an absolute path, since Sonic Pi is executing from a different working directory.
    sample(os.path.realpath(SAMPLE_FILE), rate=rate, amp=amp)
    sleep(beats * 60 / bpm)


def stop():
    """Stops all tracks."""
    msg = osc_message_builder.OscMessageBuilder(address='/stop-all-jobs')
    msg.add_arg('SONIC_PI_PYTHON')
    msg = msg.build()
    synthServer.client.send(msg)

atexit.register(stop)  # stop all tracks when the program exits normally or is interrupted

# These are the piano key numbers for a 3-octave blues scale in A. See: http://en.wikipedia.org/wiki/Blues_scale
blues_scale = [40, 43, 45, 46, 47, 50, 52, 55, 57, 58, 59, 62, 64, 67, 69, 70, 71, 74, 76]
beats_per_minute = 45				# Let's make a slow blues solo

play_note(blues_scale[0], beats=1, bpm=beats_per_minute)
