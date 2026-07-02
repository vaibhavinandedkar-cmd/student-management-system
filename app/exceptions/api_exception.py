class APIException(Exception):
    """
    Base API Exception.
    """

    def __init__(
        self,
        message="Application Error",
        status_code=400,
        errors=None
    ):
        self.message = message
        self.status_code = status_code
        self.errors = errors

        super().__init__(self.message)
