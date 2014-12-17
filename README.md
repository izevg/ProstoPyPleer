# ProstoPyPleer

Library for access to ProstoPleer (pleer.com)

## Description

This library provides full access to ProstoPleer (pleer.com) API.

Described classes:

* `Pleer` - the main essence describing functions of work with ProstoPleer's (pleer.com) API

Described methods:

* `get_access_token` - method for recieving app token from pleer.com with your Pleer.com App ID and Secret Key
* `search_for_track` - method for searching tracks by given params
* `get_track_info` - method for recieving track info by track ID, recieved in search_for_track results
* `get_download_link` - method for recieving link for track downloading or listening

## Details
Class `Pleer` contains main methods for access to ProstoPleer API.

The сonstructor of a class represents initialization of object of session with the pleer.com server and, at the 
indication of arguments of `app_id` and `app_secret_key`, receives access token for your application.

See examples below this section for more info.

- - -
`get_access_token(self, app_id, app_secret_key)` - method for recieving app token from pleer.com with your Pleer.com App ID and Secret Key

Args:
* `app_id` - ID of your application on pleer.com
* `app_secret_key` - Secret Key of your application on pleer.com
    
Returns:
* Application access token (string)

- - -
`search_for_track(self, token, params)` - method for searching tracks by given params

Args:
* `token` - application token, recieved by get_access_token func
* `params` - search params. Read more about this params at pleer.com API
    
Returns:
* Searching results at JSON format

- - -
`get_track_info(self, token, track_id)` - method for recieving track info by track ID, recieved in 
search_for_track results

Args:
* `token` - application token, recieved by get_access_token func
* `track_id` - track ID, recieved in search_for_track result

Returns:
* Track info in JSON format

- - -
`get_download_link(self, token, track_id, reason)` - Function for recieving link for track downloading or listening

Args:
* `token` - application token, recieved by get_access_token func
* `track_id` - track ID, recieved in search_for_track result
* `reason`- reason for downloading. Can be `listen` or `save`. See more at pleer.com API

- - -
## Examples

#### Creating new Pleer() object with recieving app token:
    import pleer, vars
    
    app_id = '1234567890' # Your Application ID
    app_secret_key = 'AbCdEfGhIjKlMnOpQrSt' # Application Secret Key
    
    my_pleer = pleer.Pleer(app_id, app_secret_key) # Now app token contains in my_pleer.token variable

#### Creating new Pleer() object without automatically recieving app token:
    import pleer, vars
    my_pleer = pleer.Pleer()
    
#### Recieving __full__ tracklist by custom request (with created Pleer object as it was described earlier):
    search_result = my_pleer.search_for_track(my_pleer.token, query) # If Pleer was created with args and
    token = my_pleer.get_access_token(app_id, app_secret_key) # if not, recieving the token and
    search_result = my_pleer.search_for_track(token, query) # then recieving the tracklist
Note: `search_result` returns *full* info (including tracks count and info about each of them). To recieve only 
tracks ID's you can do something like this:
    
    tracks = search_result['tracks'] # Split search results and tracks descriptions
    track_info = tracks.keys() # Get only server tracks ID's
    for track in track_info:
        track_id = tracks[track]['id'] # And get the real ID's
#### Recieving track info (with track ID):
    tracks_info = my_pleer.get_track_info(token, track_id)

#### Recieving ling for download/listening:
    listen_link = my_pleer.get_download_link(token, track_id, 'listen') # Link for listening
    download_link = my_pleer.get_download_link(token, track_id, 'save') # And link for downloading

## Additional help
For recieving additional help send me email (to jack.zhukov@gmail.com), or write me in Jabber (izevg@jabber.ru)
