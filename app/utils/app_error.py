from fastapi import HTTPException, status


class PasswordError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "code": 401001,
                "result": {"error": "Password error."}
            }
        )


class TokenAuthenticateFailed(HTTPException):
    def __init__(self, e) -> None:
        super().__init__(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail={
                "code": 402001,
                "result": {"error": f"Failed to authenticate token, {e}"}
            }
        )


class NotTodoListOwner(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail={
                "code": 402002,
                "result": {"error": "User isn't todo list's owner."}
            }
        )


class UsernameExistedError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": 403001,
                "result": {"error": "Username existed."}
            }
        )


class UserNotExistedError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": 403002,
                "result": {"error": "User not existed."}
            }
        )


class EmailExistedError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": 403003,
                "result": {"error": "Email existed."}
            }
        )


class TodoListNotExisted(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": 403004,
                "result": {"error": "Todo list not existed."}
            }
        )


class NoTokenError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": 403005,
                "result": {"error": "No token provided."}
            }
        )


class UsernamePasswordError(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": 404001,
                "result": {"error": "Username or Password error."}
            }
        )


class OperationFailed(HTTPException):
    def __init__(self, e) -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "code": 500001,
                "result": {"error": f"Operation failed.{e}"}
            }
        )
