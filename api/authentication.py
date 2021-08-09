from datetime import datetime, timedelta
import jwt

SECRET = 'LAKSLSOAISKJDKASPDJASMCKASPI'

def account_does_not_exists(request):
    return False

def password_is_not_valid(request):
    return False

def generate_token(request):
    return jwt.encode({'username': request.get_json().get('vat', None),
                       'exp': datetime.utcnow() + timedelta(hours=24)},
                        SECRET,
                        algorithm='HS256').decode('UTF-8')

def decode_vat(request):

        authorization_header = request.headers.get(
                'Authorization', 'x x').split()

        assert authorization_header[0] == 'Bearer'

        token = authorization_header[1]
        claim = jwt.decode(token, SECRET, algorithms=['HS256'])
        return claim.get('username')