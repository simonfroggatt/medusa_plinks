from django.shortcuts import render
from django.conf import settings

import json
import requests
import webbrowser
import base64
import datetime
import os
from . import xeromanager
from . import xeroobjects

# Create your views here.
client_id = '93451C96C8EF447194E02AEE28BAF124'
client_secret = 'tLoGvLNzNjnEcsqCetBuXWgZxB9DVU1ueONtyR3hMXC9ZuKu'
redirect_url = 'https://localhost:8000/xero/passback/'
scope = 'offline_access accounting.settings accounting.contacts'
b64_id_secret = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')
access_token = {'refresh_token': '', 'expiry': ''}


def XeroFirstLogin(request):
    template_name = 'xero_onetime.html'

    auth_url = ('''https://login.xero.com/identity/connect/authorize?''' +
                '''response_type=code''' +
                '''&client_id=''' + client_id +
                '''&redirect_uri=''' + redirect_url +
                '''&scope=''' + scope +
                '''&state=123''')

    webbrowser.open_new(auth_url)
    #opens new window for login to XERO for first access

    return render(request, template_name)


def XeroGetTokenInfo(request):
    template_name = 'xero_onetime.html'

    auth_code = request.GET['code']

    #Exchange the code
    exchange_code_url = 'https://identity.xero.com/connect/token'
    response = requests.post(exchange_code_url,
                             headers={
                                 'Authorization': 'Basic ' + b64_id_secret
                             },
                             data={
                                 'grant_type': 'authorization_code',
                                 'code': auth_code,
                                 'redirect_uri': xeromanager.constants.XERO_REDIRECT_URL
                             })

    if response.status_code == 200:
        json_response = response.json()
        return_val = {'response:': 200, 'access_token': json_response['access_token'],
                      'refresh_token': json_response['refresh_token']}
        token_file = os.path.join(settings.BASE_DIR, 'apps/xero_toolkit/' + xeromanager.constants.XERO_TOKEN_FILENAME)
        with open(token_file, 'w') as outfile:
            json.dump(json_response, outfile)

    else:
        token_file = os.path.join(settings.BASE_DIR, 'apps/xero_toolkit/' + xeromanager.constants.XERO_TOKEN_FILENAME + '.error')
        with open(token_file, 'w') as outfile:
            outfile.write(response.text)
        return_val = {'response': response.status_code, 'access_token': response.status_code, 'refresh_token': response.reason}


    # response.status_code =='200'
 #   print(json_response)
 #   print('\n')

    return render(request, template_name, return_val)


def XeroFirstAuth():
    # 1. Send a user to authorize your app
    auth_url = ('''https://login.xero.com/identity/connect/authorize?''' +
                '''response_type=code''' +
                '''&client_id=''' + client_id +
                '''&redirect_uri=''' + redirect_url +
                '''&scope=''' + scope +
                '''&state=123''')

    webbrowser.open_new(auth_url)

    # 2. Users are redirected back to you with a code

    auth_res_url = 'https://www.xero.com/uk/?code=7f5958f3d60dfd3e8131f2b5a489d8f73b07daddba290cb66d9980636eb3a924&scope=accounting.settings&state=123'
    #auth_res_url = input('What is the response URL? ')
    start_number = auth_res_url.find('code=') + len('code=')
    end_number = auth_res_url.find('&scope')
    auth_code = auth_res_url[start_number:end_number]
  #  print(auth_code)
  #  print('\n')

    # 3. Exchange the code
    exchange_code_url = 'https://identity.xero.com/connect/token'
    response = requests.post(exchange_code_url,
                             headers={
                                 'Authorization': 'Basic ' + b64_id_secret
                             },
                             data={
                                 'grant_type': 'authorization_code',
                                 'code': auth_code,
                                 'redirect_uri': redirect_url
                             })
    json_response = response.json()
    if response.status_code == 200:
        return_val = {'response:': 200, 'access_token': json_response['access_token'], 'refresh_token': json_response['refresh_token']}
    else:
        return_val = {'response': response.status_code,'access_token': 'error', 'refresh_token': 'error'}

    if response.status_code==200:

        token_file = os.path.join(settings.BASE_DIR, 'assets/xero_token.json')
        with open(token_file, 'w') as outfile:
            json.dump(json_response, outfile)

   # print(json_response)
   # print('\n')

    # 4. Receive your tokens
    return return_val


def XeroRefreshToken():
    token_file = os.path.join(settings.BASE_DIR, 'assets/xero_token.json')
    with open(token_file) as json_file:
        data = json.load(json_file)
    old_token = data['refresh_token']
    token_refresh_url = 'https://identity.xero.com/connect/token'
    response = requests.post(token_refresh_url,
                             headers={
                                 'Authorization': 'Basic ' + b64_id_secret,
                                 'Content-Type': 'application/x-www-form-urlencoded'
                             },
                             data={
                                 'grant_type': 'refresh_token',
                                 'refresh_token': old_token
                             })
    json_response = response.json()
   # print(json_response)

    new_refresh_token = json_response['refresh_token']
    #rt_file = open('C:/folder/refresh_token.txt', 'w')
    #rt_file.write(new_refresh_token)
    #rt_file.close()

    token_file = os.path.join(settings.BASE_DIR, 'assets/xero_token.json')
    with open(token_file, 'w') as outfile:
        json.dump(json_response, outfile)

    return json_response['access_token']


def XeroTenants(access_token):
    connections_url = 'https://api.xero.com/connections'
    response = requests.get(connections_url,
                            headers={
                                'Authorization': 'Bearer ' + access_token,
                                'Content-Type': 'application/json'
                            })
    json_response = response.json()
   # print(json_response)

    for tenants in json_response:
        json_dict = tenants
    return json_dict['tenantId']


def XeroRequestCompany(request):
#
    template_name = 'test.html'
    context = {'test':'just a test'}
   # old_tokens = XeroTestGetAccessToken()
    new_tokens = XeroRefreshToken()
    xero_tenant_id = XeroTenants(new_tokens)

    get_url = 'https://api.xero.com/api.xro/2.0/Contacts?where=Name.Contains("fred")'
    response = requests.get(get_url,
                            headers={
                                'Authorization': 'Bearer ' + new_tokens,
                                'Xero-tenant-id': xero_tenant_id,
                                'Accept': 'application/json'
                            })

    json_response = response.json()
    print(json_response)
    print('\n')

    return render(request, template_name, context)


def XeroTestGetAccessToken():
    token_file = os.path.join(settings.BASE_DIR, 'assets/xero_token.json')
    with open(token_file) as json_file:
        data = json.load(json_file)
    return data['access_token']


def XeroPutContact(request):

    template_name = 'test.html'
    context = {'test': 'just a test or put contact'}

    xero_contact = xeroobjects.XeroContact()
    contact_data = {'xero_id' : '12345'}
    xero_contact.create_contact(contact_data)
    print(xero_contact)
    return render(request, template_name, context)


def GetContactDetails():
    contactinfo = dict()
    ContactPerson = dict()
    contactinfo['Name'] = "Test name"
    contactinfo['FirstName'] = "Simon"
    contactinfo['LastName'] = "Froggatt"
    contactinfo['EmailAddress'] = "simon@Bloggs.com"
    contactinfo['IsCustomer'] = "true"

    ContactPerson['FirstName'] = "Joe"
    ContactPerson['LastName'] = "Bloggs"
    ContactPerson['EmailAddress'] = "joe@Bloggs.com"

    contactinfo['ContactPersons'] = [1]
    contactinfo['ContactPersons'][0] = ContactPerson

    contacts = [1]
    contacts[0] = contactinfo
    contact = {"Contacts": contacts}
    return contact


def XeroTestClass(request):
    template_name = 'test.html'
    context = {'test': 'just a test'}

    xero_c = xeromanager.XeroAuthManager()
    if xero_c.has_tokens():
        if xero_c.get_company_name():
            xero_company_data = xero_c.get_xero_response()
            company_data = xero_company_data['Organisations'][0]
            context['xero_test'] = company_data['Name']
        else:
            xero_errors = xero_c.get_error()
            context['xero_errors'] = xero_errors

    else:
        xero_errors = xero_c.get_error()
        context['xero_errors'] = xero_errors


    return render(request, template_name, context)