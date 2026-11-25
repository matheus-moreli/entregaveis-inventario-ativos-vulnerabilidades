from datetime import datetime, timedelta, timezone
from hashlib import sha256
from hmac import compare_digest
from secrets import token_urlsafe

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from argon2.low_level import Type

HASHER = PasswordHasher(type=Type.ID)
EMISSOR = "inventario-ufu-lab"
AUDIENCIA = "inventario-ufu-lab-api"


def guardar_senha(senha: str) -> str:
    return HASHER.hash(senha)


def verificar_senha(hash_armazenado: str, senha: str) -> bool:
    try:
        return HASHER.verify(hash_armazenado, senha)
    except VerifyMismatchError:
        return False


def emitir_chave_api() -> tuple[str, str]:
    chave = token_urlsafe(32)
    return chave, sha256(chave.encode()).hexdigest()


def verificar_chave_api(chave: str, hash_armazenado: str) -> bool:
    return compare_digest(sha256(chave.encode()).hexdigest(), hash_armazenado)


def emitir_jwt(usuario: str, segredo: str) -> str:
    agora = datetime.now(timezone.utc)
    claims = {
        "sub": usuario,
        "iss": EMISSOR,
        "aud": AUDIENCIA,
        "iat": agora,
        "exp": agora + timedelta(minutes=10),
    }
    return jwt.encode(claims, segredo, algorithm="HS256")


def verificar_jwt(token: str, segredo: str) -> str:
    claims = jwt.decode(
        token,
        segredo,
        algorithms=["HS256"],
        issuer=EMISSOR,
        audience=AUDIENCIA,
        options={"require": ["sub", "iss", "aud", "iat", "exp"]},
    )
    return claims["sub"]
