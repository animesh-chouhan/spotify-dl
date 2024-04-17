import os
import time
from math import ceil
from random import shuffle

import wave
import requests
import pyaudio
import spotipy
from pydub import AudioSegment
from spotipy.oauth2 import SpotifyOAuth

from spotify_api import get_user_playlists, get_playlist_tracks
from utils import format_timespan


# Initializing audio stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
)
print("PyAudio initialized")

playlist_id = "3g1iUuKMZX3Nfg3e3Hzdi7"
output_dir = "outputs/PlaylistName"


def record(track_name, record_seconds, tags):
    print(f"* Recording {track_name}")
    frames = []
    # Buffer seconds to avoid clipping(you can play around with this)
    record_seconds += 4
    # Aligning to the start for accurate recording
    # os.system("xdotool key XF86AudioPrev")
    for _ in range(ceil(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Done recording")

    wav_path = f"{output_dir}/{track_name}.wav"
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

    wav_audio = AudioSegment.from_wav(wav_path)
    wav_audio.export(
        f"{output_dir}/Music/{track_name}.mp3",
        format="mp3",
        bitrate="320k",
        tags=tags,
        cover=f"{output_dir}/Thumbnails/{track_name}.jpg",
    )


scope = "playlist-read-private,user-read-currently-playing,user-read-recently-played,user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# playlists = get_user_playlists(sp)
# print(playlists)

with open(f"{output_dir}/downloaded.txt") as f:
    downloaded = set(f.read().splitlines())
    # print(downloaded)


tracks = get_playlist_tracks(sp, playlist_id)
tracks_to_download = [track for track in tracks if track["id"] not in downloaded]
shuffle(tracks_to_download)
total_duration = sum([track["duration"] for track in tracks_to_download]) / 1000
left_duration = total_duration
print(f"Enjoy {len(tracks_to_download)} songs, {format_timespan(ceil(total_duration))}")

for track in tracks_to_download:
    track_id = track["id"]
    track_name = track["name"]
    duration = track["duration"] / 1000
    # duration = 20
    image_url = track["image_url"]
    tags = {
        "title": track["name"],
        "album": track["album"],
        "artist": track["artist"],
    }

    with open(f"{output_dir}/Thumbnails/{track_name}.jpg", "wb") as f:
        f.write(requests.get(image_url).content)

    try:
        sp.pause_playback()
    except:
        print("Nothing playing.")
    sp.start_playback(uris=[track["uri"]])
    print(f"\nPlaying {track_name} {duration}s")
    # Handling the spotify latency
    time.sleep(3)
    record(track["name"], duration, tags)
    try:
        sp.pause_playback()
    except:
        print("Nothing playing.")
    time.sleep(3)
    left_duration -= duration
    print(f"\nTime left: {format_timespan(ceil(left_duration))}")
    with open(f"{output_dir}/downloaded.txt", "a") as f:
        f.write(track_id + "\n")

print("Done, enjoy!")

# Closing stream
stream.stop_stream()
stream.close()
p.terminate()
