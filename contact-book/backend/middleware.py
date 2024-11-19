from functools import wraps
from auth import decode_token

def authenticate(func):
    """Middleware to authenticate requests."""
    @wraps(func)
    def wrapper(event, context):
        headers = event.get("headers", {})
        token = headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return {"statusCode": 401, "body": "Unauthorized"}
        try:
            decode_token(token)
        except ValueError as e:
            return {"statusCode": 401, "body": str(e)}
        return func(event, context)
    return wrapper

def cors_headers(response):
    """
    Adds CORS (Cross-Origin Resource Sharing) headers to the response.

    This function modifies the response dictionary by adding a headers key,
    which contains several HTTP headers related to CORS. These headers 
    are used to control how resources are shared between different origins.

    Parameters:
    response (dict): The HTTP response object that will be returned to the client.

    Returns:
    dict: The modified response object with added CORS headers.
    """
    # Add CORS headers to the response
    response["headers"] = {
        # Allow all origins to access the resource
        "Access-Control-Allow-Origin": "*",
        # Specify which headers can be used in the request
        "Access-Control-Allow-Headers": "Authorization, Content-Type",
        # Specify which HTTP methods are allowed when accessing the resource
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
    }
    # Return the modified response
    return response
