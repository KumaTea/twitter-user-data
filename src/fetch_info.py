from session import kuma


def get_info(user_id, slim=True):
    result = kuma.get_user(user_id)
    if slim:
        delattr(result, 'status')
        delattr(result, '_api')
        delattr(result, '_json')
    return result
