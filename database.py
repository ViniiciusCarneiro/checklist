import pyodbc
from config import SERVER, DATABASE, DRIVER, TRUSTED_CONNECTION

def conectar_banco():
    try:
        conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection={TRUSTED_CONNECTION};Connection Timeout=120;')
        return conn
    except Exception as e:
        raise
def salvar_item(conn, item):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM items WHERE itemId = ?", (item['itemId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO items (itemId, checklistId, categoryId, name, deletedAt, [order])
            VALUES (?, ?, ?, ?, ?, ?)
        """, (item['itemId'], item['checklistId'], item['categoryId'], item['name'], item['deletedAt'], item['order']))

        conn.commit()
        return 1
    except Exception as e:
        raise


def salvar_categoria(conn, categoria):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Categories WHERE categoryId = ?", (categoria['categoryId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        created_at = categoria['createdAt'][:-6]
        updated_at = categoria['updatedAt'][:-6]

        deleted_at = categoria['deletedAt'][:-6] if categoria['deletedAt'] else None

        cursor.execute("""
            INSERT INTO categories (categoryId, checklistId, parentId, type, name, description, createdAt, updatedAt, deletedAt, category_order)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (categoria['categoryId'], categoria['checklistId'], categoria['parentId'], categoria['type'],
              categoria['name'], categoria['description'], created_at, updated_at, deleted_at,
              categoria['order']))

        conn.commit()
        return 1
    except Exception as e:
        raise


def salvar_action_plan(conn, action_plan):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Actions WHERE actionPlanId = ?", (action_plan['actionPlanId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute(""" 
            INSERT INTO Actions (
                actionPlanId, parentId, evaluationId, checklistId, unitId,
                userId, categoryId, itemId, resultId, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", action_plan['actionPlanId'], action_plan.get('parentId'),
            action_plan['evaluationId'], action_plan['checklistId'], action_plan['unitId'], action_plan['userId'],
            action_plan['categoryId'], action_plan['itemId'], action_plan['resultId'], action_plan['status'],)
        conn.commit()

        return 1
    except Exception as e:
        raise
