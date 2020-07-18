def is_exist(request, s_name):
    if( None == request.session.get(s_name, None)):
        return False
    else:
        return True

def get_session(request, s_name):
    if not is_exist(request, s_name):
        return False
    else:
        return request.session[s_name]

def delete_session(request, s_name):
    if not is_exist(request, s_name):
        return False
    else:
        del request.session[s_name]

def print_session(request):
    for key, value in request.session.items():
        print(str(key) + " : " + str(value))

def set_session(request, s_name, data):
     request.session[s_name] = data






    

    
