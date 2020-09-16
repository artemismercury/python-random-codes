def cap_song_repetition(playlist, song):
    '''(list, string) -> list

    Return a playlist after removing, from left to right, the repetitive song which exceeds 3
    times being played.

    >>> cap_song_repetition(['A', 'B', 'B', 'C', 'D', 'C', 'B', 'A', 'C', 'B', 'A', 'B'], 'B')
    ['A', 'C', 'D', 'C', 'B', 'A', 'C', 'B', 'A', 'B']

    '''
  
    while playlist.count(song) > 3:
        playlist.remove(song)

    print(playlist)

def cap_song_repetition_1(playlist, song):
    '''(list, string) -> list

    Return a playlist after removing, from left to right, the repetitive song which exceeds 3
    times being played.

    >>> cap_song_repetition_1(['A', 'B', 'B', 'C', 'D', 'C', 'B', 'A', 'C', 'B', 'A', 'B'], 'B')
    ['A', 'C', 'D', 'C', 'B', 'A', 'C', 'B', 'A', 'B']

    '''

    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))
        
    print(playlist)
