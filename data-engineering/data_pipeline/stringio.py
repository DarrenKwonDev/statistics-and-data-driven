from io import StringIO
import csv

in_memory_file = StringIO()
csv_writer = csv.writer(in_memory_file)
csv_writer.writerows([[1, 2, 3], [4, 5, 6]])
in_memory_file.seek(0)
for row in in_memory_file:
    print(row)
