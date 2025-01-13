'''
https://prepare.sh/interview/devops/6753945e3d80ca2fb7d0a8c1

A development team has encountered an issue with their Python application: it fails to accurately retrieve and display SSL certificate information for their web services. Your task is to implement and verify the check_cert_expiry function to resolve this problem.
Task:

Write a Python function named check_cert_expiry(hostname, port=443) that takes a hostname (e.g., "example.com") and an optional port number as input. The function should perform the following actions:

    Establish a secure SSL connection to the specified hostname and port.
    Retrieve the SSL certificate from the server.
    Extract the certificate's expiry date (notAfter field) and calculate the number of days remaining until the certificate expires.
    Extract the issuer information from the certificate.
    Return a dictionary containing the following keys:
        hostname: The input hostname.
        expiry_date: The expiry date formatted as "YYYY-MM-DD".
        days_remaining: The number of days remaining until the certificate expires.
        issuer: A dictionary representing the certificate issuer's details.

Expected Outcome:

The check_cert_expiry function should successfully connect to the specified host, retrieve and parse the SSL certificate, and return accurate information regarding the certificate's expiry date, days remaining, and issuer. The function should handle exceptions gracefully, providing meaningful error messages when failures occur (e.g., connection issues, invalid hostnames).

    All provided examples should pass successfully.
    The implementation should follow best coding practices and handle edge cases appropriately.

Example answer:

import datetime
import ssl
import socket

def check_cert_expiry(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(..
            # Your code here
            return {
                'hostname': hostname,
                'expiry_date': expiry_date.strftime('%Y-%m-%d'),
                'days_remaining': days_remaining,
                'issuer': issuer
            }
		
Examples
Example #1

Input:
check_cert_expiry('python.org')

Possible Output:

{
  "hostname": "python.org",
  "expiry_date": "2024-04-15",
  "days_remaining": 200,
  "issuer": {
    "commonName": "Let's Encrypt Authority X3",
    "organizationName": "Let's Encrypt",
    "countryName": "US"
  }
}

Example #2

Input:
check_cert_expiry('github.com')

Possible Output:

{
  "hostname": "github.com",
  "expiry_date": "2024-06-30",
  "days_remaining": 250,
  "issuer": {
    "commonName": "DigiCert TLS Hybrid ECC SHA384 2020 CA1",
    "organizationName": "DigiCert Inc",
    "countryName": "US"
  }
}

Example #3

Input:
check_cert_expiry('invalid.example.com')

Possible Output:

Error checking invalid.example.com: [Errno -2] Name or service not known
'''
import datetime
import ssl
import socket

def check_cert_expiry(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            days_remaining = (expiry_date - datetime.datetime.now()).days
            return {
                'hostname': hostname,
                'expiry_date': expiry_date.strftime('%Y-%m-%d'),
                'days_remaining': days_remaining,
                'issuer': dict(x[0] for x in cert['issuer'])
            }

a = check_cert_expiry('python.org')
print(a)