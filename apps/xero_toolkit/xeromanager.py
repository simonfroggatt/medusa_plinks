from django.conf import settings

from . import constants

import json
import requests
import webbrowser
import base64
import datetime
import os


class XeroAuthManager:

    refresh_token = ''
    access_token = ''
    refresh_timestamp = 0
    refresh_timeout = 1800
    token_filename = ''
    b64_id_secret = ''
    tenant_id = ''
    status_code = 0
    error_codes = {}
    xero_return_data = {}
    valid_xero = False

    def __init__(self):
        self.token_filename = os.path.join(settings.BASE_DIR, 'apps/xero_toolkit/'+constants.XERO_TOKEN_FILENAME)
        self.b64_id_secret = base64.b64encode(
            bytes(constants.XERO_CLIENT_ID + ':' + constants.XERO_CLIENT_SECRET, 'utf-8')).decode('utf-8')
        self.refresh_timestamp = datetime.datetime.now()
        self._get_refresh_token()

    def xero_setup_token_info(self, auth_code):

        # auth_code = request.GET['code']

        exchange_code_url = 'https://identity.xero.com/connect/token'
        response = requests.post(exchange_code_url,
                                 headers={
                                     'Authorization': 'Basic ' + self.b64_id_secret
                                 },
                                 data={
                                     'grant_type': 'authorization_code',
                                     'code': auth_code,
                                     'redirect_uri': constants.XERO_REDIRECT_URL
                                 })

        if response.status_code == 200:
            json_response = response.json()
            with open(self.token_filename, 'w') as outfile:
                json.dump(json_response, outfile)
        else:
            self.__process_errors(response, exchange_code_url)

    def get_company_name(self):
        self. _get_req('Organisation','','')
        return self.valid_xero
        #self. _get_req('freds','','')

    def set_contact_details(self, contact_data):
        self._set_req('Contacts', '', '')

    def save_to_xero(self, endpoint, xero_data):
        self._set_req(endpoint, xero_data, '')
        return self.valid_xero

    def has_tokens(self):
        return self.valid_xero

    def has_xero_data(self):
        return self.valid_xero

    def get_error(self):
        return self.error_codes

    def get_xero_response(self):
        return self.xero_return_data

    def _get_refresh_token(self):
        if os.path.isfile(self.token_filename) == False:
            self._xero_first_login()
        else:
            self._xero_refresh_token()

    def _xero_first_login(self):
        auth_url = ('''https://login.xero.com/identity/connect/authorize?''' +
                    '''response_type=code''' +
                    '''&client_id=''' + constants.XERO_CLIENT_ID +
                    '''&redirect_uri=''' + constants.XERO_REDIRECT_URL +
                    '''&scope=''' + constants.XERO_SCOPE +
                    '''&state=123''')

        webbrowser.open_new(auth_url)

    def _xero_refresh_token(self):

        with open(self.token_filename) as json_file:
            data = json.load(json_file)

        dt_exp = self.refresh_timestamp
        dt_now = datetime.datetime.now()

        if dt_now > dt_exp:
            old_token = data['refresh_token']
            token_refresh_url = 'https://identity.xero.com/connect/token'
            response = requests.post(token_refresh_url,
                                     headers={
                                         'Authorization': 'Basic ' + self.b64_id_secret,
                                         'Content-Type': 'application/x-www-form-urlencoded'
                                     },
                                     data={
                                         'grant_type': 'refresh_token',
                                         'refresh_token': old_token
                                     })
            if response.status_code == 200:
                json_response = response.json()
                with open(self.token_filename, 'w') as outfile:
                    json.dump(json_response, outfile)

                self.refresh_timeout = json_response['expires_in']
                self.refresh_timestamp = dt_now + datetime.timedelta(seconds=self.refresh_timeout)
                self.access_token = json_response['access_token']
                self.valid_xero = True
            else:
                self.__process_errors(response, token_refresh_url)
        else:
            self.access_token = data['access_token']

        if self.tenant_id == '':
            self._xero_tenants()

    def _xero_tenants(self):
        connections_url = 'https://api.xero.com/connections'
        response = requests.get(connections_url,
                                headers={
                                    'Authorization': 'Bearer ' + self.access_token,
                                    'Content-Type': 'application/json'
                                })
        if response.status_code == 200:
            json_response = response.json()
            for tenants in json_response:
                json_dict = tenants
            self.tenant_id = json_dict['tenantId']
        else:
            self.__process_errors(response, connections_url)

    def _get_req(self, url_endpoint, data, filters):
        self._xero_refresh_token()

        get_url = constants.XERO_BASE_URL + url_endpoint
        response = requests.get(get_url,
                                headers={
                                    'Authorization': 'Bearer ' + self.access_token,
                                    'Xero-tenant-id': self.tenant_id,
                                    'Accept': 'application/json'
                                })

        if response.status_code == 200:
            json_response = response.json()
            if json_response['Status'] == 'OK':
                self.xero_return_data = json_response
            else:
                self.valid_xero = False
                self.status_code = json_response['Status']
        else:
            self.__process_errors(response, url_endpoint)

    def _set_req(self, url_endpoint, data, filters):
        self._xero_refresh_token()
        post_url = constants.XERO_BASE_URL + url_endpoint
        print(data)

        tmp = json.dumps(data, default=str)
        log_file = os.path.join(settings.BASE_DIR, 'apps/xero_toolkit/postlog.json')
        with open(log_file, 'w') as outfile:
            json.dump(data, outfile, default=str)

        response = requests.post(post_url,
                                 data=json.dumps(data, default=str),
                                 headers={
                                     'Authorization': 'Bearer ' + self.access_token,
                                     'Xero-tenant-id': self.tenant_id,
                                     'Content-type': 'application/json',
                                     'Accept': 'application/json'
                                 })

        if response.status_code == 200:
            json_response = response.json()
            if json_response['Status'] == 'OK':
                self.xero_return_data = json_response
            else:
                self.valid_xero = False
                self.status_code = json_response['Status']
        else:
            self.__process_errors( response, 'post' + url_endpoint)

    def __process_xero_response(self, json_response, endpoint):
        self.valid_xero = False

    def __process_errors(self, response, error_process):
        self.valid_xero = False
        self.status_code = response.status_code
        self.error_codes['error_type']= response.reason
        self.error_codes['error_process'] = error_process
        self.error_codes['error_code'] = response.status_code

  #      log_file = os.path.join(settings.BASE_DIR, 'apps/xero_toolkit/xero_error.log')
  #      if os.path.exists(log_file):
  #          append_write = 'a'  # append if already exists
  #      else:
  #          append_write = 'w'  # make a new file if not

  #      with open(log_file, append_write) as outfile:
  #          outfile.write(error_process + "response:" + response + '\n')


       # self.error_codes['error_number'] = json_response['status']
        #self.error_codes['error_type'] = json_response['type']
        #self.error_codes['error_detail'] = json_response['detail']
