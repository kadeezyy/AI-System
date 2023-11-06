import requests
import urllib3
import json
from typing import Optional, Dict

# Suppress the SSL/TLS related warning
urllib3.disable_warnings()


class Requester:
    def __init__(self, host_url: str, data: Optional[Dict] = None):
        self.host_url = host_url
        self.headers = {
            "Content-Type": "application/json"
        }
        self.data = data

        def authenticate(username, password) -> str:
            return self.send_request(
                http_method='post',
                url="https://id.itmo.ru/auth/realms/itmo/login-actions/authenticate",
                data={
                    "username": username,
                    "password": password
                }
            )

        self.headers["Authorization"] = authenticate("341474", "31p6hd19")
        print(self.headers["Authorization"])

    def send_request(self, http_method: str, url: Optional[str] = None, data: Optional[Dict] = None,
                     params: Optional[Dict] = None):
        try:
            if http_method == 'get':
                response = requests.get(url, headers=self.headers, params=params)
            elif http_method == 'post':
                response = requests.post(url, data=data, headers=self.headers, params=params)
            elif http_method == 'put':
                response = requests.put(url, data=data, headers=self.headers, params=params)
            elif http_method == 'delete':
                response = requests.delete(url, headers=self.headers, params=params)
            else:
                return None  # Unsupported HTTP method

            print(f"Response status code = {response.status_code}")
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get_request(self, params: Optional[Dict] = None):
        return self.send_request(url=self.host_url, http_method='get', params=params)

    def post_request(self, data: dict, params: Optional[Dict] = None):
        return self.send_request(url=self.host_url, http_method='post', data=data, params=params)


class Saver:
    def __init__(self, response):
        self.response_data = response
        print(response)

    def save_data_to_file(self):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self.response_data.json(), f, ensure_ascii=False, indent=4)

    def convert_json_to_csv(self):
        pass


if __name__ == "__main__":
    # url = "https://my.itmo.ru/api/schedule/schedule/personal?date_start=2023-10-30&date_end=2023-11-05"
    url = "https://id.itmo.ru/auth/realms/itmo/login-actions/authenticate"

    token = (
        "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIwSVliSmNVLW1wbEdBdzhFMzNSNkNKTUdWa3hZdUQ2eUItdWt3RlBJOXV3In0.eyJleHAiOjE2OTkxMTYwODgsImlhdCI6MTY5OTExNDI4OCwiYXV0aF90aW1lIjoxNjk5MTE0Mjg3LCJqdGkiOiI0ZTM0M2VhMC03ZDU1LTQ1ZjEtOTZjOC03MWNjNjQwZGEyMDIiLCJpc3MiOiJodHRwczovL2lkLml0bW8ucnUvYXV0aC9yZWFsbXMvaXRtbyIsImF1ZCI6InlhbmRleCIsInN1YiI6IjA4Y2Q5NTcxLTY4ZmItNDUzYi1iMmVhLTRmYzQ1ZDI2ZWE5OCIsInR5cCI6IkJlYXJlciIsImF6cCI6InN0dWRlbnQtcGVyc29uYWwtY2FiaW5ldCIsInNlc3Npb25fc3RhdGUiOiIyYjdlYjhmMS03ZTg0LTRmOTktOWE3Mi0wOTI3YmQ5NTE1YjciLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cHM6Ly9teS5pdG1vLnN1IiwiaHR0cHM6Ly9teS5pdG1vLnJ1IiwiaHR0cHM6Ly9lbWJlZC5pZm1vLnJ1IiwiaHR0cHM6Ly9pc3UuaWZtby5ydSJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsieWFuZGV4Ijp7InJvbGVzIjpbImVkaXQ6YWNjb3VudCJdfSwic3R1ZGVudC1wZXJzb25hbC1jYWJpbmV0Ijp7InJvbGVzIjpbImFjY2VzcyJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZWR1IHdvcmsiLCJzaWQiOiIyYjdlYjhmMS03ZTg0LTRmOTktOWE3Mi0wOTI3YmQ5NTE1YjciLCJpc3UiOjM0MTQ3NCwicHJlZmVycmVkX3VzZXJuYW1lIjoiaWQzNDE0NzQifQ.DHm6c1q3e3dGGuajDko0rfjLLapH4cl1_YSNFBvY1gY4kecOyI7FMAFLaynjntj3W5hsABiJN4ALXJDYrIDC6iYUkaLwJmFJJ3mWnA7Rm_epL1JsTbH7FPVfgjQmfB8t2oXJjl4L4-6m6nOnjF9eqLoZFaGddvCmTB0O8C8U49ViAUtF2gchfx8XSaGg2JLPIlnmuQLnvJLdzfNeipL3J7KdgDimAE5S9nob3c5Ju0MIw6aBvGz0GFFZ4CNRWyFBxtYJLDRiXfRApRAnBMS04gjCKXfenvPNnp169lUP8PozwJmKU_CCGdTIIHJr-41w_rOSmciKvEcC84HjCgWOwg")
    requester = Requester(host_url=url)
    response = requester.get_request()
    print(response)
    saver = Saver(response=response)
