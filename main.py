from api_client import APIClient
from database import conectar_banco, salvar_item, salvar_categoria, salvar_action_plan
from log_excel import log_to_excel

def main():
    conn_banco = conectar_banco()

    api_client = APIClient()
    log_file = "log_insercao.xlsx"

    items = api_client.get_items()
    total_linhas_items = 0

    for item in items:
        linhas_inseridas = salvar_item(conn_banco, item)
        total_linhas_items += linhas_inseridas

    log_to_excel(log_file, "items", total_linhas_items)

    categorias = api_client.get_categorias()
    total_linhas_categorias = 0

    for categoria in categorias:
        linhas_inseridas = salvar_categoria(conn_banco, categoria)
        total_linhas_categorias += linhas_inseridas

    log_to_excel(log_file, "categories", total_linhas_categorias)

    actionPlans = api_client.get_action_plan()
    total_linhas_action_plans = 0

    for actionPlan in actionPlans:
        linhas_inseridas = salvar_action_plan(conn_banco, actionPlan)
        total_linhas_action_plans += linhas_inseridas

    log_to_excel(log_file, "actions", total_linhas_action_plans)

    conn_banco.close()

if __name__ == "__main__":
    main()
