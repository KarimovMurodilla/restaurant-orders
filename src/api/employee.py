from fastapi import APIRouter

from api.dependencies import UOWDep

from services.employee import EmployeeService
from schemas.employee import EmployeeSchema


router = APIRouter(
    prefix="/employee",
    tags=["Employees"],
)


@router.post("/")
async def add_employee(
    uow: UOWDep,
    employee: EmployeeSchema
):
    employee_id = await EmployeeService().add_employee(uow, employee)
    return {"employee_id": employee_id}
