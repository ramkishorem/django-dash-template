import urllib.request
import urllib.parse

from django.conf import settings

def send_sms_api_call(apikey, numbers, message, sender=None):
    data_dict = {
        'apikey': apikey,
        'numbers': numbers,
        'message' : message
    }
    if sender: #only for transactional messages
        data_dict['sender'] = sender
    data =  urllib.parse.urlencode(data_dict)
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    response = urllib.request.urlopen(request, data)
    return response.read().decode("utf-8")

def send_sms(numbers, message):
    """
    numbers, if single number is just a string version of the number
    with country code. eg : '919876543210'
    """
    if settings.DEBUG:
        return 'success'
    return send_sms_api_call(settings.TXTLCL_API_KEY,
        numbers, message, settings.TXTLCL_NAME)
