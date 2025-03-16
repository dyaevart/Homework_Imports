from application.salary import calculate_salary
from application.db.people import get_employees
import pyjokes

if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print(pyjokes.get_joke())