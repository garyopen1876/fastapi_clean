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
