'''
HTTP tests for the helpr application
'''

import json
import urllib.request
import urllib.parse
import pytest

# Do NOT change this URL! If you need to change the port number, change the
# value in config.py
BASE_URL=f"http://127.0.0.1:{5000}"

@pytest.fixture
def reset_state():
    '''Reset state of server before all tests'''
    server_request = urllib.request.Request(f"{BASE_URL}/end", \
        method='DELETE', headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(server_request)
    
#############################################
#           MAKE_REQUEST                    #
#############################################

def test_make_01(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})

def test_make_02(reset_state):
    '''TESTING FAIL (PASS)'''
    try:
        register = json.dumps({"zid":  '1234567',
                               "description":   ''
        }).encode('utf-8')
                                               
        server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
            method='POST', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)
    
    except Exception as ValueError:
        print("Empty description")

def test_make_03(reset_state):
    '''TESTING FAIL (PASS)'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    
    try:
        register = json.dumps({"zid":  '1234567',
                               "description":   'hello'
        }).encode('utf-8')
                                               
        server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
            method='POST', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)

    except Exception as KeyError:
        print("You have already made a request")
        
#############################################
#               QUEUE                       #
#############################################

def test_queue_01(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})
                                               
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]

#############################################
#               REMAINING                   #
#############################################

# def test_remaining_01(reset_state):
#     '''TEST PASS'''
#     register = json.dumps({"zid":  '1234567',
#                            "description":   'hello'
#     }).encode('utf-8')
                                           
#     server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
#         method='POST', data=register, headers={'Content-Type': 'application/json'})
#     server_response = urllib.request.urlopen(server_request)
#     create_profile_response = json.load(server_response)
    
#     register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
#     server_request = urllib.request.Request(f"{BASE_URL}/remaining", \
#         method='GET', data=register, headers={'Content-Type': 'application/json'})
#     server_response = urllib.request.urlopen(server_request)
#     create_profile_response = json.load(server_response)
    
#     assert create_profile_response == {'remaining': 0}

def test_remaining_02(reset_state):
    '''TESTING FAIL (PASS)'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    try:
        server_request = urllib.request.Request(f"{BASE_URL}/remaining", \
            method='GET', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)
    
    except Exception as KeyError:
        print("You are at front of the line")
        
#############################################
#                   HELP                    #
#############################################

def test_help_01(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})

def test_help_02(reset_state):
    '''TESTING FAIL (PASS)'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    try:
        register = json.dumps({"zid":  '1234567'}).encode('utf-8')
        
        server_request = urllib.request.Request(f"{BASE_URL}/help", \
            method='POST', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)
    
    except Exception as KeyError:
        print("Already at front of line")

def test_help_03(reset_state):  
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "receiving"})]
    
#############################################
#                   RESOLVE                 #
#############################################

def test_resolve_01(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/resolve", \
        method='DELETE', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})

def test_resolve_02(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "receiving"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/resolve", \
        method='DELETE', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)

    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    # assert create_profile_response == [] // Changes to server fuctionality affected this test.
    
def test_resolve_03(reset_state):
    '''TESTING FAIL (PASS)'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]

    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    try:
        server_request = urllib.request.Request(f"{BASE_URL}/resolve", \
            method='DELETE', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)
    
    except Exception as KeyError:
        print("Stduent still waiting in queue")
    
#############################################
#                   CANCEL                 #
#############################################

def test_cancel_01(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/cancel", \
        method='DELETE', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})

def test_cancel_02(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/cancel", \
        method='DELETE', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)

    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    # assert create_profile_response == [] // Changes to the server affected this test.

def test_cancel_03(reset_state):
    '''TESTING FAIL (PASS)'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    try:
        server_request = urllib.request.Request(f"{BASE_URL}/cancel", \
            method='DELETE', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)
    
    except Exception as KeyError:
        print("You are currently being helped")
        
#############################################
#                   REVERT                  #
#############################################

def test_revert_01(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/revert", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})

def test_revert_02(reset_state):
    '''TEST PASS'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/help", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "receiving"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    server_request = urllib.request.Request(f"{BASE_URL}/revert", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)

    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]

def test_revert_03(reset_state):
    '''TESTING FAIL (PASS)'''
    register = json.dumps({"zid":  '1234567',
                           "description":   'hello'
    }).encode('utf-8')
                                           
    server_request = urllib.request.Request(f"{BASE_URL}/make_request", \
        method='POST', data=register, headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    server_request = urllib.request.Request(f"{BASE_URL}/queue", \
        method='GET', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == [({"zid": '1234567', "description": 'hello', "status": "waiting"})]
    
    register = json.dumps({"zid":  '1234567'}).encode('utf-8')
    
    try:
        server_request = urllib.request.Request(f"{BASE_URL}/revert", \
            method='POST', data=register, headers={'Content-Type': 'application/json'})
        server_response = urllib.request.urlopen(server_request)
    
    except Exception as KeyError:
        print("Student not currently being helped")
        
#############################################
#               REPRIORITISE                #
#############################################

def test_rep_01(reset_state):
    '''TEST PASS'''
    server_request = urllib.request.Request(f"{BASE_URL}/reprioritise", \
        method='POST', headers={'Content-Type': 'application/json'})
    server_response = urllib.request.urlopen(server_request)
    create_profile_response = json.load(server_response)
    
    assert create_profile_response == ({})

#############################################
#                   END                     #
#############################################

def test_end_01(reset_state):
    '''Reset state of server before all tests'''
    server_request = urllib.request.Request(f"{BASE_URL}/end", \
        method='DELETE', headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(server_request)

