import re
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import CommonPasswordValidator
from django.contrib.auth.models import User

def validation_password(password_data):
    
    if len(password_data) <8:
            raise ValidationError(
                'A senha deve conter pelo menos 8 caracteres!'
            )
        
    if not re.search(r"\d", password_data):
        raise ValidationError(
            'A senha deve conter pelo menos um numero!'
        )
        
    if not re.search(r"[A-Z]", password_data):
        raise ValidationError(
            'A senha deve conter pelo menos uma letra maiuscula!'
        )
        
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password_data):
        raise ValidationError(
            'A senha deve conter pelo menos um caractere especial (!@#$%^&*...).'
        )
        
    # Verificando se senha é muito comum
    validator = CommonPasswordValidator()
    try:
        validator.validate(password_data)
    except ValidationError:
        raise ValidationError(
            'Esta senha é muito comum. Por favor digite outra senha!'
        )
    
        
    return password_data


def validation_username(username):
    
    if User.objects.filter(username=username).exists():
        raise ValidationError(
            'Nome de usuario nao disponivel!'
        )
        
    if len(username) <3:
        raise ValidationError(
            'Nome de usuario deve conter pelo menos 3 caracteres'
        )
        
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        raise ValidationError(
            'O nome de usuario deve conter apenas letras, numeros e _'
        )
        
    if username.isdigit():
        raise ValidationError(
            'Nomde nao pode conter apenas numeros!'
        )
    
    return username