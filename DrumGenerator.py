import numpy as np 
from utils import load_wav

from detection import stereo_to_mono

class DrumGenerator:

    def __init__(self, fs=44100):
        
        self._fs = fs
        self.load_samples()
        
    # TODO: Getters (?) and setters for drum sounds

    def load_samples(self): 
        """
        Loads samples from file ./drum_samples/
        File should include files bass_drum.wav, snare_drum.wav 
        and hi_hat.wav
        """
        path = 'drum_samples/'

        fs_bass, bass_drum = load_wav(path + 'bass_drum.wav')
        self._bass_drum = stereo_to_mono(bass_drum)

        fs_snare, snare_drum = load_wav(path + 'snare_drum.wav')
        self._snare_drum = stereo_to_mono(snare_drum)

        fs_hi_hat, hi_hat = load_wav(path + 'hi_hat.wav')
        self._hi_hat = stereo_to_mono(hi_hat)

        # Checking if loaded samples have matching sampling frequency with the set fs
        error_msg = ' sample does not have matching sample frequency'
        assert fs_bass == self._fs, 'Bass drum' + error_msg
        assert fs_snare == self._fs, 'Snare drum' + error_msg
        assert fs_hi_hat == self._fs, 'hi hat' + error_msg


    def generate_drum_audio(self, hit_indices, hit_strengths, array_size):
        """
        Adds snare sounds at each index in hit_indices.
        """

        # TODO: Make snare and hihats possible (at least snare, not sure
        # how hi-hiat would be represented from the pad)

        # TODO: Enable hit_strengths to scale the sounds

        drum_audio = np.zeros(array_size)

        snare_size = self._snare_drum.size

        # TODO: Make new sounds add to array, not overwrite it
        for index in hit_indices:
            drum_audio[index:index+snare_size] = self._snare_drum

        return drum_audio
