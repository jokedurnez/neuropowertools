def get_session_id(request):
    '''get_session_id gets the user session id, and creates one if it doesn't exist'''

    if not request.session.exists(request.session.session_key):
        request.session.create()
    sid = request.session.session_key
    return(sid)