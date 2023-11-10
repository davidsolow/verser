import os
from dotenv import load_dotenv
import requests

def get_policies(**context):
    load_dotenv()
    base_url = f'https://api.congress.gov/v3/bill'
    query_params = {
        'api_key': os.getenv('CONGRESSAPI'),
        'format': 'json',
        'limit': 1,
        'offset': 0
    }

    response = requests.get(base_url, params=query_params)
    if response.status_code == 200:
        data = response.json()
        new_policies = []
        for bill in data['bills']:
            new_policies.append({'policy_id': bill['number'],
                                'policy_name': bill['title'],
                                'policy_branch': bill['originChamberCode'],
                                'policy_type': bill['type'],
                                'policy_url': bill['url'],
                                'policy_text': 'Placeholder text.'}
            )
        return new_policies
    else:
        print(f"Failed to fetch policies: {response.status_code}")
        return []