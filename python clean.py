from urllib.parse import urlparse, parse_qs, urlencode

def remove_query_param(url, param):
    """Remove a query parameter from a URL."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if param in query_params:
        del query_params[param]
    new_query = urlencode(query_params, doseq=True)
    new_url = parsed_url._replace(query=new_query).geturl()
    return new_url

# Example usage
url = "https://example.com/page?param1=value1&param2=value2&param3=value3"
new_url = remove_query_param(url, "param2")
print(new_url)
# Output: https://example.com/page?param1=value1&param3=value3
