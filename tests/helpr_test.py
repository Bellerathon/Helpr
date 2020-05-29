'''
Tests for the core functionality of the helpr application
'''

# Don't change this import line below. If your tests are black-box tests then
# you don't require any more functions from the module than these
from helpr import make_request, queue, remaining, help, resolve, cancel, revert, reprioritise, end

import pytest

def test_wat():
    assert 1 == 1
    
def test_sanity():
    '''
    A simple sanity test of the system.
    '''
    # DO NOT CHANGE THIS TEST! If you feel you have to change this test then
    # your functions have not been implemented correctly.
    student1 = "z1234567"
    description1 = "I don't understand how 'global' works in python"
    student2 = "z7654321"
    description2 = "What's the difference between iterator and iterable?"

    # Queue is initially empty
    assert queue() == []

    # Student 1 makes a request
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    assert remaining(student1) == -1

    # Student 2 makes a request
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    assert remaining(student1) == -1
    assert remaining(student2) == 0

    # Student 1 gets help
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    # Student 2 is now the only student "waiting" in the queue, so they have no
    # one remaining in front of them
    assert remaining(student2) == -1

    # Student 1 has their problem resolved
    resolve(student1)
    # Only student 2 is left in the queue
    assert queue() == [{"zid": student2, "description": description2, "status": "waiting"}]

    # Student is helped and their problem is resolved
    help(student2)
    resolve(student2)
    assert queue() ==[]

    # End the session
    end()
    

#############################################
#           MAKE_REQUEST                    #
#############################################

def test_make_01():
    'Test description is empty'
    
    student1 = "z1234567"
    description1 = ""
    
    with pytest.raises(ValueError):
        make_request(student1, description1)
    
    end()


def test_make_02():
    'Test student is already in queue'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    # Make 1st request
    make_request(student1, description1)

    with pytest.raises(KeyError):
        make_request(student1, description1)
    
    end()
    
def test_make_03():
    'Test pass case'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    # Make 1st request
    make_request(student1, description1)

    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    
    end()  

#############################################
#                   QUEUE                   #
#############################################

def test_queue_01():
    'Test queue is filling correctly'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    student2 = "z7654321"
    description2 = "Help me 2"
    
    student3 = "z7651234"
    description3 = "Help me 3"
    
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    
    make_request(student3, description3)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"},
                       {"zid": student3, "description": description3, "status": "waiting"}]
   
    end()
        
#############################################
#                   REMAINING               #
#############################################

def test_remaining_01():
    'Test correct status'
    
    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    help(student1)
    
    with pytest.raises(KeyError):
        remaining(student1)
    
    end()

def test_remaining_02():
    'Test correct status'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    student2 = "z7654321"
    description2 = "Help me 2"
    
    make_request(student1, description1)
    make_request(student2, description2)
    
    assert remaining(student2) == 0
    
    end()

#############################################
#                   HELP                    #
#############################################

def test_help_01():
    'Test already being helped'
    
    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    help(student1)
    
    with pytest.raises(KeyError):
        help(student1)
    
    end()

def test_help_02():
    'Test pass case'
    
    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    help(student1)
    
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"}]
    
    end()
    
#############################################
#                   RESOLVE                 #
#############################################

def test_resolve_01():
    'Test dequeue but not helped yet'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    student2 = "z7654321"
    description2 = "Help me 2"
    
    make_request(student1, description1)
    make_request(student2, description2)
    
    with pytest.raises(KeyError):
        resolve(student2)
    
    end()

def test_resolve_02():
    'Test pass case'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    make_request(student1, description1)
    help(student1)
    resolve(student1)
    
    assert queue() == []
    
    end()
    
#############################################
#                   CANCEL                 #
#############################################

def test_cancel_01():
    'Test cancel while being helped'

    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    help(student1)
    

    with pytest.raises(KeyError):
        cancel(student1)
    
    end()

def test_cancel_02():
    'Test pass case'

    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    
    cancel(student1)
    
    assert queue() == []
    
    end()
    
#############################################
#                   REVERT                  #
#############################################

def test_revert_01():
    'Test revert but not being helped'
    
    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    
    with pytest.raises(KeyError):
        revert(student1)
    
    end()

def test_revert_02():
    'Test pass case'
    
    student1 = "z1234567"
    description1 = "Help me"
      
    make_request(student1, description1)
    
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    
    help(student1)
    
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"}]
    
    revert(student1)
    
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    
    end()
    
#############################################
#               REPRIORITISE                #
#############################################

def test_rep_01():
    'Test pass case'
    
    reprioritise()
    
    end()
    
#############################################
#                   END                     #
#############################################

def test_end_01():
    'Test end wipes all data'
    
    student1 = "z1234567"
    description1 = "Help me"
    
    student2 = "z7654321"
    description2 = "Help me @"
    
    make_request(student1, description1)
    make_request(student2, description2)
    
    end()
    
    assert queue() == []
    
    end()





