# AUTOGENERATED! DO NOT EDIT! File to edit: 50-audio-training.ipynb (unless otherwise specified).

__all__ = ['timestamp2index']

# Cell
#modeling imports
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification, pipeline, TrainingArguments, Trainer
from datasets import load_metric
import torch
import soundfile as sf
import torch
import librosa

#ds imports
import pandas as pd
import numpy as np

#python imports
import os.path
import glob
import re
import warnings

# Cell
def timestamp2index(ts, round_type = 'ceil', sampling_rate=16000):
    '''
    Function timestamp2index: converts a timestamp with format dd:dd.ddd to an index given the sampling rate
        ts: string of timestamp in
        round_type (default 'ceil'): string of rounding to perform; can be 'ceil' or 'floor'
        sampling_rate (default 16000): integer of the sampling rate (in Hz) of the audio
    Returns: integer of index of converted timestamp or None if formatted incorrectly
    '''

    #define regex
    ts_pat = re.compile('(\d{1,2}):(\d{1,2}).(\d{1,3})')

    #get the match
    ts_match = ts_pat.match(ts)

    #throw a warning if you have issues
    if ts_match is None:
        warnings.warn('There is an issue with value: {0} and it could not be converted.'.format(ts))
        return None

    #convert to full time (note that ljust zero pads on the right)
    ts_seconds = 60*int(ts_match.group(1)) + int(ts_match.group(2)) + int(ts_match.group(3).ljust(3,'0'))/1000

    #identify rounding type
    round_func = np.ceil
    if round_type == 'floor':
        round_func = np.floor

    #create index and apply rounding
    ts_ind = int(round_func(ts_seconds * sampling_rate))

    return ts_ind