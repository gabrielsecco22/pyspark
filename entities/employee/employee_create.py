import csv
from dataclasses import fields, astuple
from timeit import default_timer as timer

from entities.employee.employee import Employee

start = timer()
start_partial = timer()
N = 10000000
PARTIAL_SIZE = 10000
with open(f'employees_{N}.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow([field.name for field in fields(Employee)])  # header row
    for i in range(N):
        csv_writer.writerow(list(astuple(Employee())))
        if i % PARTIAL_SIZE == 0:
            end_partial = timer()
            print(f"progress: {100*i/N}% - {end_partial - start_partial} (s) - remaining: {(end_partial - start_partial) * (N-i)/PARTIAL_SIZE} (s)")
            start_partial = timer()
end = timer()
# Print the execution time
print('Execution time (seconds):', end - start)