from miditime.miditime import MIDITime
import argparse
from soundParametersCreator import soundParametersCreator

parser = argparse.ArgumentParser()
parameters = []
creator = soundParametersCreator()
args = []

# parametres of the sound are made using some strings as keys
parser.add_argument('answ1', type=str)
parser.add_argument('answ2', type=str)
parser.add_argument('answ3', type=str)
parser.add_argument('answ4', type=str)
parser.add_argument('answ5', type=str)
parser.add_argument('answ6', type=str)
parser.add_argument('path', type=str)
parser.add_argument('levelOfNarcoticness', type=int)
args = parser.parse_args()

parameters += creator.createParameter(args.answ1, args.levelOfNarcoticness)
parameters += creator.createParameter(args.answ2, args.levelOfNarcoticness)
parameters += creator.createParameter(args.answ3, args.levelOfNarcoticness)
parameters += creator.createParameter(args.answ4, args.levelOfNarcoticness)
parameters += creator.createParameter(args.answ5, args.levelOfNarcoticness)
parameters += creator.createParameter(args.answ6, args.levelOfNarcoticness)

mymidi = MIDITime(100, args.path)
mymidi.add_track(parameters)
mymidi.save_midi()