playlist = {
    'title': 'Rock Leve',
    'author': 'Code-Repeat',
    'songs': [
        {'title': 'Wake Me Up When September Ends', 'artist': ['Billie Joe Armstrong'], 'duration': 2.59},
        {'title': 'Living In A Ghost Town', 'artist': ['The Rolling Stones'], 'duration': 4.07},
        {'title': 'Caburé', 'artist': ['Scalene'], 'duration': 3.09},
        {'title': 'American Reckoning', 'artist': ['Bon Jovi'], 'duration': 4.41},
        {'title': 'Tudo Que Eu Consegui', 'artist': ['Frejat'], 'duration': 3.10},
        {'title': 'O Vento - Ao Vivo', 'artist': ['Los Hermanos'], 'duration': 3.41},
        {'title': 'Wasted On You', 'artist': ['Evanescence'], 'duration': 4.24},
        {'title': 'Fire In Bone', 'artist': ['The Killers'], 'duration': 3.11},
    ]

}

#  Display the titles

for tit in playlist['songs']:
    print(f"* {tit['title']} - {' - '.join(tit['artist'])}")

#  Show total songs durations

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(f"Total duration: {round(total_length, 1)} minutes")


