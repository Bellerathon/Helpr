'''
A flask server for the backend of the 'helpr' application.

GET routes are passed arguments as URL parameters. POST and DELETE routes are
passed arguments as JSON data in the body of the request. All routes return data
as JSON.
'''

from flask import Flask, request, render_template

from werkzeug.exceptions import BadRequest

from json import dumps

from helpr import make_request, queue, remaining, help, resolve, cancel, revert, end

APP = Flask(__name__)

@APP.route('/')
def index():
    return render_template('new.html')

@APP.route('/admin')
def admin_page():
    return render_template('admin.html')

@APP.route('/hello/', methods=['GET', 'POST'])
def hello_world():
    return dumps('Hfef')

@APP.route('/make_request', methods=['POST'])
def make_request_svr():
    '''
    A route for helpr.make_request()

    Params: {"zid", "description"}

    Raises: BadRequest if helpr.make_request() raises a KeyError or ValueError.

    Returns: {}
    '''
    
    data = request.get_json()
    zid = data["zid"]
    description = data["description"]

    try:
        make_request(zid, description)
    except KeyError as key_err:
        raise KeyError(description=key_err)
    except ValueError as val_err:
        raise ValueError(description=val_err)
    else:
        return dumps({})


@APP.route('/queue', methods=['GET'])
def queue_svr():
    '''
    A route for helpr.queue()

    Returns: A list in the same format as helpr.queue()
    '''
    
    queue_data = queue()

    return dumps(queue_data)

@APP.route('/remaining/', methods=['GET'])
def remaining_svr():
    '''
    A route for helpr.remaining()

    Params: ("zid")

    Raises: BadRequest if helpr.remaining() raises a KeyError.

    Returns: { 'remaining': n } where n is an integer
    '''
    
    data = request.form.get('zid')

    try:
        num = remaining(data)
    except KeyError as key_err:
        raise KeyError(description=key_err)
    
    return dumps(num)

@APP.route('/help', methods=['POST'])
def help_svr():
    '''
    A route for helpr.help()

    Params: {"zid"}

    Raises: BadRequest if helpr.help() raises a KeyError.

    Returns: {}
    '''
    
    data = request.get_json()
    zid = data["zid"]

    try:
        help(zid)
    except KeyError as key_err:
        raise KeyError(description=key_err)
    else:
        return dumps({})

@APP.route('/resolve', methods=['DELETE'])
def resolve_svr():
    '''
    A route for helpr.resolve()

    Params: {"zid"}

    Raises: BadRequest if helpr.resolve() raises a KeyError.

    Returns: {}
    '''
    
    data = request.json

    try:
        resolve(data)
    except KeyError as key_err:
        raise KeyError(description=key_err)
    else:
        return dumps({})

@APP.route('/cancel', methods=['DELETE'])
def cancel_svr():
    '''
    A route for helpr.cancel()

    Params: {"zid"}

    Raises: BadRequest if helpr.cancel() raises a KeyError.

    Returns: {}
    '''
    
    data = request.json

    try:
        cancel(data)
    except KeyError as key_err:
        raise KeyError(description=key_err)
    else:
        return dumps({})

@APP.route('/revert', methods=['POST'])
def revert_svr():
    '''
    A route for helpr.revert()

    Params: {"zid"}

    Raises: BadRequest if helpr.revert() raises a KeyError.

    Returns: {}
    '''
    
    data = request.get_json()
    zid = data["zid"]

    try:
        revert(zid)
    except KeyError as key_err:
        raise KeyError(description=key_err)
    else:
        return dumps({})

@APP.route('/reprioritise', methods=['POST'])
def reprioritise_svr():
    '''
    A route for helpr.reprioritise()

    Returns: {}
    '''
    return dumps({})

@APP.route('/end', methods=['DELETE'])
def end_svr():
    '''
    A route for helpr.end()

    Returns: {}
    '''
    end()
    return dumps({})


if __name__ == "__main__":
    # Do NOT change the port below. If you need to change the port number do so
    # by changing the value in config.py
    APP.run(port=5000, debug=True)