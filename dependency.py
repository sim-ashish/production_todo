from fastapi import Depends, HTTPException, Cookie, status
from typing_extensions import Annotated
from typing import Union


def check_user_cookie(user: Annotated[Union[int, None], Cookie()] = None):
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Login required")
    return user