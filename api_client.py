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
            endpoint = f"/v1/items?page={page}&limit={limit}"

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
            endpoint = f"/v1/categories?page={page}&limit={limit}"

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

            endpoint = f"/v1/action-plans?page={page}&limit=1000"

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

    def get_checklists(self, page=1):
        all_tickets = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/checklists?page={page}&limit=1000"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            tickets = data.get('data', [])

            if not tickets:
                break

            all_tickets.extend(tickets)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_tickets

    def get_evaluations(self, page=1):
        all_evaluations = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/evaluations?page={page}&limit=1000"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            evaluations = data.get('data', [])

            if not evaluations:
                break

            all_evaluations.extend(evaluations)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_evaluations

    def get_users(self, page=1):
        all_users = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/users?page={page}&limit=1000"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            users = data.get('data', [])

            if not users:
                break

            all_users.extend(users)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_users

    def get_units(self, page=1):
        all_units = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/units?page={page}&limit=1000"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            units = data.get('data', [])

            if not units:
                break

            all_units.extend(units)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_units

    def get_departamentos(self, page=1):
        all_departamentos = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/departments?page={page}&limit=1000"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            departamentos = data.get('data', [])

            if not departamentos:
                break

            all_departamentos.extend(departamentos)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_departamentos

    def get_user_types(self, page=1):
        all_user_types = []

        while True:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"
            }

            endpoint = f"/v1/user-types?page={page}&limit=1000"

            self.connection.request("GET", endpoint, "", headers)
            response = self.connection.getresponse()

            if response.status != 200:
                print(f"Erro: {response.status} {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            user_types = data.get('data', [])

            if not user_types:
                break

            all_user_types.extend(user_types)

            has_more = data.get('meta', {}).get('hasMore', False)

            if not has_more:
                break

            page += 1

        return all_user_types



