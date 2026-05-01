import pygame

musics = [
    "music/track1.wav" , "music/track2.wav"
]

index_music = 0

def play_music():
    pygame.mixer.music.load(musics[index_music])

    pygame.mixer.music.play()

def stop_music():
    
    pygame.mixer.music.stop()

def next_music():

    global index_music 
    index_music += 1

    if index_music >= len(musics):
        index_music = 0

    play_music()

def prev_music():
    
    global index_music

    index_music -= 1

    if index_music < 0:
        index_music = len(musics) - 1

    play_music()

def track_info():
    
    return musics[index_music]


