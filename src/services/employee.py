from schemas.employee import EmployeeSchema
from utils.unitofwork import IUnitOfWork

from db.mongodb import MongoDBManager
from utils.repository import MongoDBRepository

class EmployeeService:
    def __init__(self):
        self.mongodb = MongoDBManager.client["restaurants"]
        self.employees = MongoDBRepository(self.mongodb["employees"])

    async def add_employee(self, uow: IUnitOfWork, data: EmployeeSchema):
        data_dict = data.model_dump()
        async with uow:
            employee_id = await uow.employee.add_one(data_dict) # PostgreSQL
            await self.employees.add_one(data_dict) # MongoDB
            await uow.commit()
            return employee_id

    async def get_employee(self, uow: IUnitOfWork, employee_id: int):
        # async with uow:
            # order = await uow.employee.find_one(employee_id=employee_id)
        order = await self.employees.find_one(employee_id=employee_id)
        return order
