import random
from datetime import date, timedelta
from datetime import datetime
from faker import Faker

fake = Faker(locale='en_US')
from dataclasses import dataclass, field


@dataclass
class Employee:
    badge: str = field(default_factory=lambda: str(random.randrange(1, 1000000000)).zfill(9))
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    department: str = field(default_factory=lambda: random.choice(Employee.dept))
    phone: str = field(default_factory=fake.phone_number)
    salary_cents: str = field(default_factory=lambda: str(random.randrange(3500000, 25000000)))
    bonus_rate: str = field(default_factory=lambda: str(random.randrange(20, 150) / 100))
    birthday: str = field(default_factory=lambda: fake.date_of_birth(minimum_age=18, maximum_age=75).strftime("%Y-%m-%d"))
    state: str = field(default_factory=fake.state_abbr)
    zipcode: str = field(init=False)
    email: str = field(init=False)
    start_date: str = field(init=False)

    # Auxiliary field
    dept = ['IT', 'HR', 'Finance', 'Procurement', 'Operations', 'Marketing', 'Sales', 'Customer Support']

    # Defining field-dependant values
    def __post_init__(self):
        try:
            self.zipcode = fake.zipcode_in_state(state_abbr=self.state)
            self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"
            delta = timedelta(days=random.randrange(1, self.get_age_days() - 18*365))
            self.start_date = fake.date_between_dates(date_start=date.today() - delta, date_end=date.today()).strftime("%Y-%m-%d")
        except Exception as e:
            self.start_date = fake.date_between_dates(date_start=date.today() - delta, date_end=date.today()).strftime(
                "%Y-%m-%d")
    def get_age_days(self):
        return (datetime.today() - datetime.strptime(self.birthday, "%Y-%m-%d")).days


