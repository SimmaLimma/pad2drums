from DrumGenerator import DrumGenerator

from detection import detect_sound

from utils import load_wav, save_wav

def pad2drums(read_from_fname, save_to_fname):
    """
    Reads .wav-file in folder "raw_audio" from a drum pad (with mic about 10 cm away)
    and converts it to an .wav-file with drum sounds in place of 
    the pad sounds. Created file is placed in folder "results".
    """

    load_path = 'raw_audio/'
    fs, raw_audio = load_wav(load_path + read_from_fname)

    # Detecting the pad hits from the raw_audio
    hit_indices, hit_strengths = detect_sound(raw_audio, stereo=True)
    
    dg = DrumGenerator(fs=fs)
    drum_audio = dg.generate_drum_audio(hit_indices, hit_strengths, sig.size):

    # Save drum_audio to file name for save_to_file added by user
    save_path = 'results/' + save_to_fname
    save_wav(file_name, drum_audio, fs)
    