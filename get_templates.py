import requests
import json
import os

token = 'eyJraWQiOiIyMzY4ZjRhYi00N2ZiLTQwN2MtYjM5Ni00NzgxODcwMjZkN2UiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJhN2VvX3NGU1dZbzAtckQzdERKZWFBIiwiY2xpZW50X2lkIjoiT0MtQVpBVXhJWUlJTmtCIiwiYXVkIjoiaHR0cHM6Ly93d3cuY2FudmEuY29tIiwiaWF0IjoxNzIxNzA2OTIwLCJuYmYiOjE3MjE3MDY5MjAsImV4cCI6MTcyMTcyMTMyMCwiYnVuZGxlcyI6WyJDVDAyIl0sInRpZXIiOiJwYWlkIiwicm9sZXMiOiJJeV82ZFFjMy1mNUU0TnhnV1RnNk00RHUyd2I3OGJiTTREMDFKQ3lUaGRyY2JNVzJUUG1rUUZWdWZnQUxUVWJ0bmFVWnZfeldPbmJfRC1oZi1jSTNnN3h4Smo3dTFkQkNyZjdvUHREcmR0ZDNhZ3NHX0NYQ2NuRFpiVEo5OXVHU1VZUHpxdyIsImxvY2FsZSI6Im1sMVAzSnJPR3dDQTQzRTlCRm1ydWhRZ0g4cEpaTlBzS3c1UVRHZkpXTzlybW5VYkFkVFktVGprWjFTNHF4a05fQ1JxOFEiLCJzY29wZXMiOlsiYXNzZXQ6cmVhZCIsImFzc2V0OndyaXRlIiwiYnJhbmR0ZW1wbGF0ZTpjb250ZW50OnJlYWQiLCJicmFuZHRlbXBsYXRlOm1ldGE6cmVhZCIsImNvbW1lbnQ6cmVhZCIsImNvbW1lbnQ6d3JpdGUiLCJkZXNpZ246Y29udGVudDpyZWFkIiwiZGVzaWduOmNvbnRlbnQ6d3JpdGUiLCJkZXNpZ246bWV0YTpyZWFkIiwiZGVzaWduOnBlcm1pc3Npb246cmVhZCIsImRlc2lnbjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnBlcm1pc3Npb246cmVhZCIsImZvbGRlcjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnJlYWQiLCJmb2xkZXI6d3JpdGUiLCJwcm9maWxlOnJlYWQiXSwic3ViIjoib1VWT2pPNjd0VjMtVFdHeEw3cWNYUSIsImJyYW5kIjoib0JWT2otcXJxT3d3LS15cDdEVXF1ZyIsIm9yZ2FuaXphdGlvbiI6bnVsbCwiY29kZV9pZCI6ImkyRnZFSkdFNkRBYUVWRFVvanRCR1EifQ.dyItPOjwgqfe7ELTyqqie4oo0-lUfS_vhB0UOzTpYmsMFf5tPEch4Yv6q5sG21ffFzfA8bH_-ltaqNM6P7t3HCFfQB7aKKdrfJD5kcFC3wKzlTYKrvvlC_tee09Ibt2sFVQP0QuRzttbvecSyL9K65vRRr8Vcc4VHbLZd2zC4sJOjJneFFh3bR66rUzRlRFZLoKxEIPJSJ40s1MybTM1v7cHLvDBi2PhhKaP-gI0obkCsnEI_F4TK52jAWAH2W6AaUxie9a0VRxm-P8B86LN3f3JUN1w4jwdMyXIHPX4_pQAauwaDyXA1dclvEYH1zI9fblMjWChcKB4m_wHW-fnsg'

def save_to_file(data, filename):
    if not os.path.exists('results'):
        os.makedirs('results')
    with open(f'results/{filename}', 'w') as f:
        json.dump(data, f, indent=4)

def get_all_templates():
    try:
        response = requests.get(
            "https://api.canva.com/rest/v1/brand-templates",
            headers={"Authorization": f"Bearer {token}"}
        )
        data = response.json()
        print("All Templates Response:")
        print(json.dumps(data, indent=4))
        save_to_file(data, 'all_templates.json')
    except requests.exceptions.RequestException as error:
        print(error)

def get_template_id(brand_template_id):
    try:
        response = requests.get(
            f"https://api.canva.com/rest/v1/brand-templates/{brand_template_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        data = response.json()
        formatted_output = {
            "id": data['brand_template']['id'],
            "title": data['brand_template']['title'],
            "view_url": data['brand_template']['view_url'],
            "create_url": data['brand_template']['create_url'],
            "thumbnail": {
                "width": data['brand_template']['thumbnail']['width'],
                "height": data['brand_template']['thumbnail']['height'],
                "url": data['brand_template']['thumbnail']['url']
            }
        }
        print("Template ID Response:")
        print(json.dumps(formatted_output, indent=4))
        save_to_file(formatted_output, f'template_{brand_template_id}.json')
    except requests.exceptions.RequestException as error:
        print(error)

# Uncomment the function call you want to see working
# get_all_templates()
get_template_id("DAGLtZh_G3c")
