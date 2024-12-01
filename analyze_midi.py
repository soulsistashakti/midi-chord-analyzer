from mido import MidiFile

def get_chord_name(notes):
    # Basic triad chords mapping
    chords = {
        (48, 52, 55): "C",
        (50, 53, 57): "D",
        (52, 55, 59): "E",
        (53, 57, 60): "F",
        (55, 59, 62): "G",
        (57, 60, 64): "A",
        (59, 62, 65): "B",
        (55, 58, 62): "Gm",  # Added G minor
        (49, 53, 56): "C#dim",  # Added C# diminished
    }
    notes = tuple(sorted(notes))
    return chords.get(notes, f"Unknown ({notes})")

def analyze_midi(file_path):
    midi = MidiFile(file_path)
    chords = []
    current_notes = []

    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:
                current_notes.append(msg.note)
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if current_notes:
                    chord_name = get_chord_name(current_notes)
                    chords.append(chord_name)
                    current_notes = []

    return chords

# File path for the MIDI file
midi_file_path = "/Users/brendabrewer/Music/GarageBand/Could it Be Intro-m-Prog.mid"

print(f"Analyzing MIDI File: {midi_file_path}")

try:
    # Analyze the MIDI file
    chords = analyze_midi(midi_file_path)
    print("Chord Progression:")
    print(chords)
except Exception as e:
    print(f"Error reading the MIDI file: {e}")

