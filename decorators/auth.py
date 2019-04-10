import logging


def auth():
    """Just a simple decorator to check whether the request is authenticated or not.

    Returns:
        It will call a wrapper function prior to the original one.

    """

    def check_auth(f):
        """Checks if user is authenticaed or not.

        Args:
            f (*): Function to be wrapped.

        Returns:
            A wrapped function.

        """

        async def wrapper(*args, **kwargs):
            """It wraps the authentication verification.

            Returns:
                The authorized function is requested is proper authorized.

            """
            
            # Check if it is allowed
            allowed = False

            # Getting handler object
            handler = args[0]

            # Gets current token
            token = handler.get_token()

            # Tries to authenticate the system
            is_auth = handler.check_auth(token)
            
        return wrapper

    return check_auth
