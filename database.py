import pyodbc
from config import SERVER, DATABASE, DRIVER, TRUSTED_CONNECTION

def conectar_banco():
    try:
        conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection={TRUSTED_CONNECTION};Connection Timeout=240;')
        return conn
    except Exception as e:
        raise
def salvar_item(conn, item):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Item WHERE itemId = ?", (item['itemId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO Item (itemId, checklistId, categoryId, name, deletedAt, [order])
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

def salvar_ticket(conn, ticket):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Checklist WHERE ChecklistId = ?", (ticket['checklistId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO Checklist (
                Checklistid, Type, Name, Description, Active, CreatedAt, UpdatedAt, DeletedAt
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", ticket['checklistId'], ticket['type'], ticket['name'],
            ticket['description'], ticket['active'], ticket['createdAt'], ticket['updatedAt'], ticket['deletedAt'],)
        conn.commit()

        return 1
    except Exception as e:
        raise

def salvar_evaluation(conn, evaluation):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Evaluation WHERE EvaluationId = ?", (evaluation['evaluationId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO Evaluation (
                EvaluationId, TableStatus, Score, ChecklistId, UnitId, UserId, StartedAt, ConcludedAt, ApprovedAt, TablePlatform,
                Scheduled, ScheduleStartDate, ScheduleEndDate, FinalComment, SharedTo, CountAttachments, InitialLatitude, InitialLongitude, FinalLatitude, FinalLongitude,
                CreatedAt, UpdatedAt, DeletedAt 
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", evaluation['evaluationId'], evaluation['status'], evaluation['score'], evaluation['checklistId'],
            evaluation['unitId'], evaluation['userId'], evaluation['startedAt'], evaluation['concludedAt'], evaluation['approvedAt'], evaluation['platform'], evaluation['scheduled'],
            evaluation['scheduleStartDate'], evaluation['scheduleEndDate'], evaluation['finalComment'], evaluation['sharedTo'], evaluation['countAttachments'], evaluation['initialLatitude'],
            evaluation['initialLongitude'], evaluation['finalLatitude'], evaluation['finalLongitude'], evaluation['createdAt'], evaluation['updatedAt'], evaluation['deletedAt'])

        conn.commit()

        return 1

    except Exception as e:
        raise

def salvar_user(conn, user):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Users WHERE UserId = ?", (user['userId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO Users (
                UserId, Name, Email, Active, UserTypeId, Phone, LanguageId, CountryId, StateId, CreatedAt,
                UpdatedAt, DeletedAt)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, user['userId'], user['name'], user['email'], user['active'], user['userTypeId'],
                    user['phone'], user['languageId'], user['countryId'], user['stateId'], user['createdAt'], user['updatedAt'], user['deletedAt'])

        conn.commit()

        return 1

    except Exception as e:
        raise

def salvar_unit(conn, unit):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Units WHERE UnitId = ?", (unit['unitId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO Units (
                UnitId, Name, Email, Active, CountryId, CreatedAt, UpdatedAt, DeletedAt) VALUES
                (?, ?, ?, ?, ?, ?, ?, ?)""", unit['unitId'], unit['name'], unit['email'], unit['active'],
                       unit['countryId'], unit['createdAt'], unit['updatedAt'], unit['deletedAt'])
        conn.commit()

        return 1

    except Exception as e:
        raise

def salvar_departamento(conn, departamento):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM Departamentos WHERE DepartmentId = ?", (departamento['departmentId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
        INSERT INTO Departamentos (
            DepartmentId, Name, Active, CreatedAt, UpdatedAt, DeletedAt) VALUES
            (?, ?, ?, ?, ?, ?)""", departamento['departmentId'], departamento['name'], departamento['active'],
                       departamento['createdAt'], departamento['updatedAt'], departamento['deletedAt'])

        conn.commit()
        return 1

    except Exception as e:
        raise

def salvar_user_type(conn, user_type):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM UserTypes WHERE UserTypeId = ?", (user_type['userTypeId'],))
        exists = cursor.fetchone()[0] > 0

        if exists:
            return 0

        cursor.execute("""
            INSERT INTO UserTypes (
                UserTypeId, Name, Active, CreatedAt, UpdatedAt,DeletedAt) VALUES
                (?, ?, ?, ?, ?, ?)""", user_type['userTypeId'], user_type['name'], user_type['active'],
                       user_type['createdAt'], user_type['updatedAt'], user_type['deletedAt'])

        conn.commit()
        return 1

    except Exception as e:
        raise
