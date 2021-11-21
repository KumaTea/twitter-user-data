from session import kuma


def get_info(user_id, slim=True):
    result = kuma.get_user(user_id=user_id)
    if slim:
        try:
            delattr(result, 'status')
        except:
            pass
        try:
            delattr(result, '_api')
        except:
            pass
        try:
            delattr(result, '_json')
        except:
            pass
    return result
