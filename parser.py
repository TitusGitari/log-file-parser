# parser.py

from datetime import datetime

# Filter by error level
print("------ ERROR Logs ------")
with open('sample.log', 'r') as file:
    for line in file:
        parts = line.strip().split(" ", 2)
        timestamp = parts[0] + " " + parts[1]
        log_level_and_message = parts[2]
        if log_level_and_message.startswith("ERROR"):
            print(f"{timestamp} - {log_level_and_message}")

# Filter by keyword
print("\n------ Logs Containing Keyword: 'database' ------")
keyword = "database"
with open('sample.log', 'r') as file:
    for line in file:
        if keyword.lower() in line.lower():
            print(line.strip())

# Filter by time range
print("\n------ Logs Between 13:46 and 13:49 ------")
start_time = datetime.strptime("2025-08-01 13:46:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime("2025-08-01 13:49:00", "%Y-%m-%d %H:%M:%S")

with open('sample.log', 'r') as file:
    for line in file:
        parts = line.strip().split(" ", 2)
        timestamp = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S")
        if start_time <= timestamp <= end_time:
            print(line.strip())
