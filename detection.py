import numpy as np

def stereo_to_mono(stereo_audio):
    """

    """

    # Not sure if this is actually left
    left_audio = stereo_audio[:, 0]
    right_audio = stereo_audio[:, 1]

    mono_audio = (left_audio + right_audio ) / 2.0 

    return mono_audio

def detect_sound(signal, stereo=False):
    """
    Checks signal (numpy array) for sounds where drum sounds
    will be placed.

    Returns numpy-array (same size as signal) with booleans, 
    False for where silence should be and True for where 
    sounds has been detected.
    """

    if stereo:
        signal = stereo_to_mono(signal)

    detected_sounds = np.zeros(signal.size)
    

    return detected_sounds