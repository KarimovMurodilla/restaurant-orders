from schemas.employee import EmployeeSchema
from utils.unitofwork import IUnitOfWork


class EmployeeService:
    async def add_employee(self, uow: IUnitOfWork, data: EmployeeSchema):
        data_dict = data.model_dump()
        async with uow:
            employee_id = await uow.employee.add_one(data_dict)
            await uow.commit()
            return employee_id

    async def get_employee(self, uow: IUnitOfWork, employee_id: int):
        async with uow:
            order = await uow.employee.find_one(employee_id=employee_id)
            return order
