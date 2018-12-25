from DrumGenerator import DrumGenerator

from detection import detect_sound

from utils import load_wav, save_wav

def pad2drums(read_from_fname, save_to_fname=''):
    """

    """

    load_path = 'raw_audio/'
    fs, sig = load_wav(load_path + read_from_fname)

    # Save drum_audio if file name for save_to_file added by user
    if save_to_file:
        save_path = 'results/'
        pass
        #save_wav(something, something)

