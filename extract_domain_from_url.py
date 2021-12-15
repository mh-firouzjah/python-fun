# import re


# def domain_name(url):
#     regex = r"((https://|http://)?(www.)?)(?P<domain>[\d\w-]+)[.].*"
#     print(url)
#     if match := re.match(regex, url):
#         return match.group('domain').split('.')[0]
#     return None


def domain_name(url):
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.replace('www.', '')
    return url.split('.')[0]

s = "3"
s.capitalize()
