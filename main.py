from api_client import APIClient
from database import conectar_banco, salvar_item, salvar_categoria, salvar_action_plan, salvar_ticket, salvar_evaluation, salvar_user, salvar_unit, salvar_departamento, salvar_user_type
from log_excel import log_to_excel
import time
import http.client

def main():
    conn_banco = conectar_banco()

    api_client = APIClient()
    log_file = "log_insercao.xlsx"

    def process_data(api_function, save_function, conn_banco, log_file, label, retries=3):
        total_linhas = 0
        for attempt in range(retries):
            try:
                data_items = api_function()
                for item in data_items:
                    linhas_inseridas = save_function(conn_banco, item)
                    total_linhas += linhas_inseridas
                log_to_excel(log_file, label, total_linhas)
                break
            except http.client.RemoteDisconnected:
                if attempt < retries - 1:
                    print(f"Tentativa {attempt + 1} falhou, tentando novamente...")
                    time.sleep(2)
                else:
                    raise
    process_data(api_client.get_items, salvar_item, conn_banco, log_file, "items")
    process_data(api_client.get_categorias, salvar_categoria, conn_banco, log_file, "categories")
    process_data(api_client.get_action_plan, salvar_action_plan, conn_banco, log_file, "actions")
    process_data(api_client.get_checklists, salvar_ticket, conn_banco, log_file, "tickets")
    process_data(api_client.get_evaluations, salvar_evaluation, conn_banco, log_file, "evaluations")
    process_data(api_client.get_users, salvar_user, conn_banco, log_file, "users")
    process_data(api_client.get_units, salvar_unit, conn_banco, log_file, "units")
    process_data(api_client.get_departamentos, salvar_departamento, conn_banco, log_file, "departments")
    process_data(api_client.get_user_types, salvar_user_type, conn_banco, log_file, "user_types")

    conn_banco.close()

if __name__ == "__main__":
    main()
