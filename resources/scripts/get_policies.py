import os
import requests
from bs4 import BeautifulSoup

def get_policies(**context):
    new_policies = [
        {
            'policy_id': '1234',
            'policy_name': 'New Bill',
            'policy_branch': 'Legislative',
            'policy_type': 'House Bill',
            'policy_url': 'www.newbill.com',
            'policy_text': 'This is a sweet new bill'
        }
    ]
    return new_policies