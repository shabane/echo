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
    
    
    def __init__(self, apiUrl: str, certSha256: str) -> None:
        self.apiUrl = apiUrl
        self.certSha256 = certSha256


    def server(self) -> dict:
        """Returns information about the server(HTTP GET)

        Returns:
            dict: 200, server information
        """
        return json.loads(self.__http_get(f'{self.apiUrl}/server/').content)

