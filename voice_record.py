import sounddevice as sd
import wavio

# Parameters
duration = 12  # Duration of recording in seconds
sample_rate = 44100  # Sample rate

print("Recording...")

# Record audio
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
sd.wait()  # Wait until recording is finished

print("Recording complete.")

# Save the recording as a WAV file
wavio.write("my_recording.wav", recording, sample_rate, sampwidth=2)

print("Recording saved as 'my_recording.wav'.")
