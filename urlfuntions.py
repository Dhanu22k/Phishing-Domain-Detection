import socket

from ipwhois import IPWhois

def get_asn_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        obj = IPWhois(ip_address)
        results = obj.lookup_whois()
        return results['asn']
    except Exception as e:
        return -1


import dns.resolver

def check_spf_record(domain):
    try:
        # Set the query type to TXT, as SPF records are typically stored in TXT records.
        records = dns.resolver.resolve(domain, "TXT")

        # Check if any record contains the "v=spf1" identifier, indicating an SPF record.
        for record in records:
            if "v=spf1" in record.to_text().lower():
                return 1
        return 0
    except dns.resolver.NXDOMAIN:
        # The domain name doesn't exist, so no SPF record can be found.
        return 0
    except dns.exception.DNSException as e:
        # Other DNS related error occurred.
        return 0

    import socket

def count_unique_ips(domain):
        try:
            ip_addresses = set()
            for ip in socket.gethostbyname_ex(domain)[2]:
                ip_addresses.add(ip)
            return len(ip_addresses)
        except Exception as e:
            return -1


import dns.resolver
import tldextract


def count_mx_servers(url):
    extracted = tldextract.extract(url)
    domain = extracted.registered_domain
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        mx_servers = set()
        for rdata in answers:
            mx_servers.add(rdata.exchange.to_text())
        return len(mx_servers)
    except Exception as e:
        print("Error from count_max_servers:", e)
        return None




import dns.resolver

def count_nameservers(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        nameservers = set()
        for rdata in answers:
            nameservers.add(rdata.to_text())
        return len(nameservers)
    except Exception as e:
        return -1

import requests


def count_redirects(url):
    try:
        # Add the scheme to the URL
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url

        response = requests.head(url, allow_redirects=True)
        return len(response.history)
    except Exception as e:
        print("Error from count_redirects:", e)
        return -1

import whois
import datetime

def get_domain_dates(domain):
    try:
        domain_info = whois.whois(domain)
        if domain_info is not None:
            registration_date = domain_info.creation_date
            expiration_date = domain_info.expiration_date
            today = datetime.datetime.now()
            if registration_date is not None and expiration_date is not None:
                if isinstance(registration_date, list):
                    registration_date = registration_date[0]
                if isinstance(expiration_date, list):
                    expiration_date = expiration_date[0]
                activation_time = (today - registration_date).days
                expiration_time = (expiration_date - today).days
                return activation_time, expiration_time
            else:
                return -1, -1
        else:
            return -1, -1
    except Exception as e:
        return -1, -1

import requests
import time

def get_time_response(url):
    try:
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url  # Add the default scheme if missing
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        return end_time - start_time
    except Exception as e:
        print("Error:", e)
        return -1

import dns.resolver

def has_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            if "v=spf1" in rdata.strings:
                return 1
        return 0
    except dns.resolver.NoAnswer:
        return 0
    except Exception as e:
        print("Error:", e)
        return None


import socket
import ssl

def has_ssl_certificate(domain):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            return 1
    except Exception as e:
        print("Error:", e)
        return 0

import dns.resolver

def get_ttl(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return answers.rrset.ttl
    except Exception as e:
        return -1


import re
import requests
from bs4 import BeautifulSoup


def is_url_google_indexed(url):
  google = "https://www.google.com/search?q=site:" + url + "&hl=en"
  response = requests.get(google, cookies={"CONSENT": "YES+1"})
  soup = BeautifulSoup(response.content, "html.parser")
  not_indexed = re.compile("did not match any documents")
  if soup(text=not_indexed):
    return 0
  else:
    return 1


import requests

def add_scheme(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url

def is_url_shortened(url):
    url=add_scheme(url)
    url = url.replace('www.', '')
    try:
        original_length = len(url)
        response = requests.head(url, allow_redirects=True)
        final_url = response.url.replace('www.','').removesuffix('/')
        final_length = len(final_url)
        if final_length>original_length:
            return 1  # URL has been shortened
        else:
            return 0  # URL has not been shortened

    except Exception as e:
        print("Error:", e)
        return 0

from urllib.parse import urlparse
def extract_domain(url):
    # Prepend http:// if no scheme is provided
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    parsed_url = urlparse(url)
    # Extracting the domain from the parsed URL
    domain = parsed_url.netloc
    # Removing www. from the domain if present
    if domain.startswith("www."):
        domain = domain[4:]
    return domain