"""
the outline apis will write here in a the class
"""
import requests
import json


class Outline():
    @staticmethod
    def __http_get(url: str) -> requests.models.Response:
        counter = 10
        res = requests.get(url, verify=False)
        while res.status_code != 200:
            res = requests.get(url, verify=False)
            counter -= 1
            if counter <= 0:
                raise ConnectionAbortedError(f'could not connect to the ApiUrl affter {counter} tries.')
        return res
    
    
    @staticmethod
    def __http_post(url: str, json_data: dict) -> requests.models.Response:
        res = requests.post(url, json=json.dumps(json_data), verify=False)
        if res.status_code != 201:
            raise ConnectionAbortedError('could not connect to the ApiUrl(HTTP POST)')
        return res
        
    
    @staticmethod
    def __http_put(url: str, json_data: dict={}, data: dict={}) -> requests.models.Response:
        res = requests.put(url, json=json_data, data=data, verify=False)
        if res.status_code != 204:
            raise ConnectionAbortedError(f'{res.status_code}: could not connect to the ApiUrl(HTTP PUT)')
        return res
    
    
    def __init__(self, apiUrl: str, certSha256: str = None) -> None:
        self.apiUrl = apiUrl
        self.certSha256 = certSha256


    def server(self) -> dict:
        """Returns information about the server(HTTP GET)

        Returns:
            dict: 200, server information
        """
        return json.loads(self.__http_get(f'{self.apiUrl}/server/').content)


    def list_access_keys(self) -> dict:
        """Lists the access keys

        Returns:
            dict: 200, Lists og access keys(HTTP GET)
        """
        return json.loads(self.__http_get(f'{self.apiUrl}/access-keys/').content)


    def new_access_key(self, name: str, usage_limit: int) -> dict:
        """Creates a new access key

        Returns:
            dict: 201, The newly created access key(HTTP POST)
        """
        __key = json.loads(self.__http_post(url=f'{self.apiUrl}/access-keys/', json_data={"method": "aes-192-gcm"}).content) # create new key
        self.__http_put(url=f'{self.apiUrl}/access-keys/{__key["id"]}/name/', data={"name": name}) # rename it
        self.__http_put(url=f'{self.apiUrl}/access-keys/{__key["id"]}/data-limit/', json_data={"limit": {"bytes": usage_limit}}) # set usage limit
        return __key


    def get_usage_limit(self) -> dict:
        return json.loads(self.__http_get(f'{self.apiUrl}/metrics/transfer/').content)


    def delete_key(self, id: int) -> bool:
        if type(id) != int:
            raise TypeError('the id should be an intiger')
        if requests.delete(f'{self.apiUrl}/access-keys/{id}/', verify=False).status_code:
            return True
        return False


    def set_date_limit(self, id: int, usage_limit: int) -> bool:
        if self.__http_put(url=f'{self.apiUrl}/access-keys/{id}/data-limit/', json_data={"limit": {"bytes": usage_limit}}):
            return True
        return False


    def set_name(self, id: int, name: str) -> bool:
        if self.__http_put(url=f'{self.apiUrl}/access-keys/{id}/name/', data={"name": name}):
            return True
        return False
