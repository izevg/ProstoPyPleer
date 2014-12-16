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

import requests
from vars import debug, methods, api_url


class Pleer:
    '''The main essence describing functions
    of work with Prostopleer's (pleer.com) API

    Attributes:
        app_id: ID of your app on pleer.com
        app_secret_key: Secret Key of your app on pleer.com
        token: access token of your app
        session: object of open session
    '''

    global session
    token = ""

    def __init__(self, app_id='', app_secret_key=''):
        '''Pleer class constructor
        Takes two arguments: app ID and app Secret Key

        Args:
            app_id: ID of your app on pleer.com
            app_secret_key: Secret Key of your app on pleer.com

        No returns
        '''

        global session, token
        session = requests.Session()
        if debug:
            print ("pleer_lib: Session opened.")
        if app_id != '' and app_secret_key != '':
            self.token = self.get_access_token(app_id, app_secret_key)
            if debug:
                print ('Token:', self.token)
        else:
            pass

    def get_access_token(self, app_id, app_secret_key):
        '''Function for recieving app token from pleer.com
        with your App ID and Secret Key

        Args:
            app_id: ID of your app on pleer.com
            app_secret_key: Secret Key of your app on pleer.com

        Returns:
            Application access token
        '''

        session_auth = (app_id, app_secret_key)
        grant_data = {"grant_type": "client_credentials"}
        request = session.post("http://api.pleer.com/token.php", auth=session_auth, data=grant_data)
        parsed_answer = request.json()
        if debug:
            print (parsed_answer['access_token'])
        return parsed_answer['access_token']

    def search_for_track(self, token, params):
        '''Function for searching tracks by given params

        Args:
            token: application token, recieved by get_access_token func
            params: search params. Read more about this params at pleer.com API

        Returns:
            Searching results at JSON format
        '''

        if debug:
            print('Searching for tracks...\n')
        access_method = methods[0]
        request_data = {
            'access_token': token,
            'method': access_method,
        }
        request_data.update(params)
        if debug:
            print (request_data)
        result = session.post(api_url, data=request_data)
        if debug:
            print (result.json())
        if debug:
            print ('Tracks finded!\n')
        return result.json()

    def get_track_info(self, token, track_id):
        '''Function for recieving track info by
        track ID, recieved in search_for_track results

        Args:
            token: application token, recieved by get_access_token func
            track_id: track ID, recieved in search_for_track result

        Returns:
            Track info in JSON format
        '''

        if debug:
            print('Getting track info...\n')
        access_method = methods[1]
        request_data = {
            'access_token': token,
            'method': access_method,
            'track_id': track_id
        }
        # request_data.update( track_id )
        if debug:
            print(request_data)
        result = session.post(api_url, data=request_data)
        if debug:
            print(result.json())
            print('Track info recieved.\n')
        return result.json()

    def get_download_link(self, token, track_id, reason):
        '''Function for recieving link for track
        downloading or listening

        Args:
            token: application token, recieved by get_access_token func
            track_id: track ID, recieved in search_for_track result
            reason: reason for downloading. Can be 'listen' or 'save'. See more
                    at pleer.com API

        Returns:
            Link and request status in JSON format
        '''

        if debug:
            print('Getting download link...')
        access_method = methods[3]
        request_data = {
            'access_token': token,
            'method': access_method,
            'track_id': track_id,
            'reason': reason
        }
        if debug:
            print(request_data)
        result = session.post(api_url, data=request_data)
        if debug:
            print(result.json())
            print('Download link recieved.\n')
        return result.json()

    def __del__(self):
        '''Pleer class destructor. Just close session.
        '''

        session.close()
        if debug:
            print("pleer_lib: Session closed.")
