import socket
import urllib
import requests

def bind_hard_coded_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind("0.0.0.0", 3000)


def send_insecure_request():
    requested_url = 'http://www.malicioushost.com'
    requests.get(requested_url, verify = False)


def download_resource_without_integrity_validation():
    resource_url = "192.168.1.10/executable.deb"
    urllib.urlretrieve(requested_url, "executable.deb")


def use_of_http_without_tls():
    requested_url = "http://www.apache.org"
    requests.get(requested_url)


def guest_connection(username = 'guest', password = ''):
    redirect_to_resource(username= 'guest', token = 'hseiq12jxwejk13')