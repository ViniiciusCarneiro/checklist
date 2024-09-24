import http.client
import json
import time
from datetime import datetime

from config import CHECKLIST_API_TOKEN

class APIClient:
    def __init__(self):
        self.connection = http.client.HTTPSConnection("api-analytics.checklistfacil.com.br")
        self.token = CHECKLIST_API_TOKEN

    def get_items(self, page=1, deletedAt='gte', limit=1000):
        all_items = []
        today = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }
            endpoint = f"/v1/items?checklistId&categoryId&deletedAt[{deletedAt}]={today}&page={page}&limit={limit}"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            items = data.get('data', [])

            if not items:
                break

            all_items.extend(items)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_items

    def get_categorias(self,page=1, type=1,updatedAt='gte', limit=1000):
        all_categorias = []
        today = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }
            #endpoint = f"/v1/categories?checklistId&parentId&type={type}&updatedAt[{updatedAt}]=2024-01-01T00:00:00Z&page={page}&limit={limit}"
            endpoint = f"/v1/categories?checklistId&parentId&type={type}&updatedAt[{updatedAt}]={today}&page={page}&limit={limit}"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            categorias = data.get('data', [])

            if not categorias:
                break

            all_categorias.extend(categorias)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_categorias

    def get_action_plan(self, page=1):
        all_action_plans = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/action-plans?evaluationId=&checklistId=&unitId=&userId=&="

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            action_plans = data.get('data', [])

            if not action_plans:
                break

            all_action_plans.extend(action_plans)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_action_plans