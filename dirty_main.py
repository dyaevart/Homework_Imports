from application.salary import *
from application.db.people import *
import pyjokes

if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print(pyjokes.get_joke())