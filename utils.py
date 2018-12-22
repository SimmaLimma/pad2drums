import pyaudio
import scipy.io.wavfile as wavfile
import numpy as np

def play(signal, fs = 44100):
    """
    Plays signal (which is np.array, preferably float 32) as audio 
    from system.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)    
    stream.write(signal.astype(np.float32).tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()


def save_wav(file_name, signal, fs):
    """
    Saves signal to file name specified in fname as
    16bit wav-file.
    Input signal should have values (-1,1 )

    fname should end with '.wav'
    """
    wavfile.write(file_name, fs, np.int16(signal/np.max(np.abs(signal)) * (2**(16)/2-1)))


def load_wav(file_name):
    """
    Loads .wav-file and returns np.array with signal and normalises.
    file_name should end with '.wav'
    Returned signal amplitude is (-1, 1).

    Returns np.array
    """
    fs, signal = wavfile.read(file_name)
    signal = np.float32(signal) / (2**(16)/2-1)
    return fs, signal