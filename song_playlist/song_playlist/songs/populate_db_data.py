from __future__ import absolute_import
import json

from .models import Song


# traverse through input json file & create readable format of input data to be inserted in database
# return readable dictionary
def input_data_creation():
    temp_data = {}
    # input json path
    filename = "C:\\Users\spatil12\Desktop\hello\hello_world\\app1\playlist.json"
    fp = open(filename)
    file_data = json.load(fp)
    fp.close()

    # populate temp_data dict data which maps all keys respectively
    # eg {'0': [id, title, danceability, .. etc], '1': [id, title, danceability,..etc]}
    for key, value in file_data.items():
        for counter in range(0, 100):
            if counter in temp_data:
                temp_data[counter].update({key: value[str(counter)]})
            else:
                temp_data[counter] = {'index': counter,
                                      key: value[str(counter)]}
    return temp_data


# insert input json into database table song
def insert_data_into_db():
    input_data = input_data_creation()
    status_msg = "Error in DB insert"
    for key, val in input_data.items():
        data = {'index': val['index'],
                'id': val['id'],
                'title': val['title'],
                'danceability': val['danceability'],
                'energy': val['energy'],
                'key': val['key'], 'loudness': val['loudness'],
                'mode': val['mode'],
                'acousticness': val['acousticness'],
                'instrumentalness': val['instrumentalness'],
                'liveness': val['liveness'],
                'valence': val['valence'],
                'tempo': val['tempo'],
                'duration_ms': val['duration_ms'],
                'time_signature': val['time_signature'],
                'num_sections': val['num_sections'],
                'num_segments': val['num_segments'],
                'song_class': val['class'],
                'num_bars': val['num_bars'],
                'star_ratings': 0}
        songs = Song(**data)
        songs.save()
        status_msg = "Data is been generated"
    return status_msg
