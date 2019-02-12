conf=Import('/bouamrene_diop_lecalvez_ranem/data/config.py')
chemin=conf.chemin()

def index(**kw):
    body = 'Received cookies'
    for cookie in COOKIE:
        body += BR() + B(cookie) + '&nbsp;' + COOKIE[cookie].value
        body += A('Erase', href="erase?name=%s" % cookie)
    form = FORM(action="set_cookie", method="post")
    form <= 'Name' + INPUT(name="name") + BR()
    form <= 'Value' + INPUT(name="value") + BR()
    form <= INPUT(Type="submit", value="Ok")
    return HTML(BODY(body + form))


def set_cookie(name, value):
    SET_COOKIE[name] = value
    SET_COOKIE[name]['path'] = chemin
    #raise HTTP_REDIRECTION('index')


def cookie_expiry_date(numdays):
    """ Returns a cookie expiry date in the required format.
    `expires` should be a string in the format "Wdy, DD-Mon-YY HH:MM:SS GMT"
    """
    from datetime import date, timedelta
    new = date.today() + timedelta(days=numdays)
    return new.strftime("%a, %d-%b-%Y 23:59:59 GMT")


def erase(name):
    SET_COOKIE[name] = ''
    SET_COOKIE[name]['path'] = chemin
    SET_COOKIE[name]['expires'] = cookie_expiry_date(-10)
    SET_COOKIE[name]['max-age'] = 0
    #raise HTTP_REDIRECTION('index')