'''
The MIT License (MIT)

Copyright (c) 2014 Eugene Zhukov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Eugene Zhukov (iZEvg)
Website: http://izevg.ru
'''

# -*- coding: utf-8 -*-
''' Simple client, wtited with ProstoPyPleer'''
import pleer
from vars import debug # Variable for debug logging

my_pleer = pleer.Pleer()

app_id = 'Insert here your App ID'
app_secret_key = 'Insert here your App Secret Key'

query = {
    'query': 'artist:Red hot chilli peppers', # Search for RHCP tracks
    'quality': 'best' # with best quality
}

my_pleer.token = my_pleer.get_access_token(app_id, app_secret_key) # Save app token locally for my_pleer
if debug:
    print(my_pleer.token)

search_result = my_pleer.search_for_track(my_pleer.token, query) # Send search request
if debug:
    print(search_result)

tracks = search_result['tracks'] # Show all search results
if debug:
    print(tracks)

track_info = tracks.keys() # Show "server" tracks ID's

for track in track_info:
    track_id = tracks[track]['id'] # Get real tracks ID's for next operations
if debug:
    print(track_id)

tracks_info = my_pleer.get_track_info(my_pleer.token, track_id) # Recieving track info
if debug:
    print(tracks_info)

download_link = my_pleer.get_download_link(my_pleer.token, track_id, 'save') # Recieving download link
if debug:
    print(download_link)
