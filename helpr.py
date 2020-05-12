'''
The core functions of the helpr application.
'''

# Put the global variables that hold the complete state of the application here.
DATA = []

def getData():
    '''Returns the global data'''
    global DATA
    return DATA
    
def make_request(zid, description):
    '''
    Used by students to make a request. The request is put in the queue with a
    "waiting" status.

    Params:
      zid (str): The ZID of the student making the request.

      description (str): A brief description of what the student needs help
      with.

    Raises:
      ValueError: if the description is the empty string.

      KeyError: if there is already a request from this particular student in
      the queue.
    '''
    
    data = getData()
            
    if description == '':
        raise ValueError("Emtpy description")
    
    for student in data:
        if student['zid'] == zid:
            raise KeyError("You have already made a request")
            
    student_data = {
        'zid': zid,
        'description': description,
        'status': "waiting"
        }
    
    data.append(student_data)
    

def queue():
    '''
    Used by tutors to view all the students in the queue in order.

    Returns:
      (list of dict) : A list of dictionaries where each dictionary has the keys
      { 'zid', 'description', 'status' }. These correspond to the student's ZID,
      the description of their problem, and the status of their request (either
      "waiting" or "receiving").
    '''
    
    data = getData()
    
    return data

def remaining(zid):
    '''
    Used by students to see how many requests there are ahead of theirs in the
    queue that also have a "waiting" status.

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: if the student does not have a request in the queue with a
      "waiting" status.

    Returns:
      (int) : The position as a number >= 0
    '''
    
    data = getData()
                
    for student in data:
        if student['zid'] == zid:
            if student['status'] != 'waiting':
                raise KeyError("Invalid status")
            
    index = 0
    for students in data:
        if students['zid'] == zid:
            break
        if students['status'] == 'waiting':
            index+=1
    
    return index
    
def help(zid):
    '''
    Used by tutors to indicate that a student is getting help with their
    request. It sets the status of the request to "receiving".

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: if the given student does not have a request with a "waiting"
      status.
    '''
    
    data = getData()
    
    for student in data:
        if student['zid'] == zid:
            if student['status'] == 'receiving':
                raise KeyError("You are already being helped")
                
    for students in data:
        if students['zid'] == zid:
            students['status'] = 'receiving'

def resolve(zid):
    '''
    Used by tutors to remove a request from the queue when it has been resolved.

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: if the given student does not have a request in the queue with a
      "receiving" status.
    '''
    
    data = getData()
    
    for student in data:
        if student['zid'] == zid:
            if student['status'] == 'waiting':
                raise KeyError("Student is still waiting")
                
    for students in data:
        if students['zid'] == zid:
            data.remove(students)
    

def cancel(zid):
    '''
    Used by students to remove their request from the queue in the event they
    solved the problem themselves before a tutor was a available to help them.

    Unlike resolve(), any requests that are cancelled are NOT counted towards
    the total number of requests the student has made in the session.

    Params:
      zid (str): The ZID of the student who made the request.

    Raises:
      KeyError: If the student does not have a request in the queue with a
      "waiting" status.
    '''
    
    data = getData()
    
    for student in data:
        if student['zid'] == zid:
            if student['status'] == 'receiving':
                raise KeyError("You're being helped currently")
        
    for students in data:
        if students['zid'] == zid:
            data.remove(students)


def revert(zid):
    '''
    Used by tutors in the event they cannot continuing helping the student. This
    function sets the status of student's request back to "waiting" so that
    another tutor can help them.

    Params:
      zid (str): The ZID of the student with the request.

    Raises:
      KeyError: If the student does not have a request in the queue with a
      "receiving" status.
    '''
    
    data = getData()
    
    for student in data:
        if student['zid'] == zid:
            if student['status'] == 'waiting':
                raise KeyError("You are not currently being helped")
                
    for students in data:
        if students['zid'] == zid:
            if students['status'] == 'receiving':
                students['status'] = 'waiting'
    
def reprioritise():
    '''
    Used by tutors toward the end of the help session to prioritize the students
    who have received the least help so far.

    The queue is rearranged so that if one student has made fewer non-cancelled
    requests than another student, they are ahead of them in the queue. The
    ordering is otherwise preserved; i.e. if a student has made the same number
    of requests as another student, but was ahead of them in the queue, after
    reprioritise() is called, they should still be ahead of them in the queue.
    '''
    #HINT: This function might be challenging to implement. You may wish to
    # leave it till after you test and implement the other functions.
    pass

def end():
    '''
    Used by tutors at the end of the help session. All requests are removed from
    the queue and any records of previously resolved requests are wiped.
    '''
    
    data = getData()
    data.clear()
    