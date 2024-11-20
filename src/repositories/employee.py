from db.models.employee import Employee
from utils.repository import SQLAlchemyRepository


class EmployeeRepository(SQLAlchemyRepository):
    model = Employee
