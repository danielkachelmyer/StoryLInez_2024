import requests
import json
import os

token = 'eyJraWQiOiIyMzY4ZjRhYi00N2ZiLTQwN2MtYjM5Ni00NzgxODcwMjZkN2UiLCJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJWVUx2akVyalBKY0laUmZPaEVWaFRRIiwiY2xpZW50X2lkIjoiT0MtQVpBVXhJWUlJTmtCIiwiYXVkIjoiaHR0cHM6Ly93d3cuY2FudmEuY29tIiwiaWF0IjoxNzIxODUyMTMyLCJuYmYiOjE3MjE4NTIxMzIsImV4cCI6MTcyMTg2NjUzMiwiYnVuZGxlcyI6WyJDVDAyIl0sInRpZXIiOiJwYWlkIiwicm9sZXMiOiJXeGx6UXZSc3ZGR0xhY084OG5IRFdJR1k4Tkl6ZWZhN0tUaHV4VHFsclhyUjkxbjI4bWdBdXgtc2xYNGdjb2tPUnU3MWZIUzl3VnJKSkEwYm9WWEVFVllsY2FTTERGaFVvdnFDa25abHFyR2xUSzZMWkx6Nm1hdUxxbWNaTnN4alF1blFLQSIsImxvY2FsZSI6Imo3a1JJTXNTVmhIa2tWeFQtUlctcXQzbC1xX2NCQk1EbUxub1o4c25uM1hCeUk4dGx6YnJuSDdYcmtMeDN1WVdId0VVUUEiLCJzY29wZXMiOlsiYXNzZXQ6cmVhZCIsImFzc2V0OndyaXRlIiwiYnJhbmR0ZW1wbGF0ZTpjb250ZW50OnJlYWQiLCJicmFuZHRlbXBsYXRlOm1ldGE6cmVhZCIsImNvbW1lbnQ6cmVhZCIsImNvbW1lbnQ6d3JpdGUiLCJkZXNpZ246Y29udGVudDpyZWFkIiwiZGVzaWduOmNvbnRlbnQ6d3JpdGUiLCJkZXNpZ246bWV0YTpyZWFkIiwiZGVzaWduOnBlcm1pc3Npb246cmVhZCIsImRlc2lnbjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnBlcm1pc3Npb246cmVhZCIsImZvbGRlcjpwZXJtaXNzaW9uOndyaXRlIiwiZm9sZGVyOnJlYWQiLCJmb2xkZXI6d3JpdGUiLCJwcm9maWxlOnJlYWQiXSwic3ViIjoib1VWT2pPNjd0VjMtVFdHeEw3cWNYUSIsImJyYW5kIjoib0JWT2otcXJxT3d3LS15cDdEVXF1ZyIsIm9yZ2FuaXphdGlvbiI6bnVsbCwiY29kZV9pZCI6Im04QzV5ZFZsVlRjUm9ZT19MM1lLdmcifQ.DgB9OAw69msUbGwbMasJV3aGG5yCRF4oGVLea8MulwpIxWvB2-BXpkNLPv_WPPkhJl0CYGXM5ELDTFvPdXknAwcLziOn_HADErDEvkZYjIQ05e7sMSuo3Fz6_QVU9HO0rD4JKdnVxX7viO2nmx_GYe5MX77N96MnXkfV2-SnUJmhjGHGt7Id584nIOkmfplcZW38MLv7SQyzRabspbglEuqF9TrWVgtKDy0VePEBucCzwrsL4RkXbB908Z7nkjRa2UKsFYiK3D6-c6I5kcOwV4lmpPOpXXGIi5fl3Aw9ilBkbijynj_QeF0T8nMOXwm1fXDUWBe5A5A0PoSZho_QaA'
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
