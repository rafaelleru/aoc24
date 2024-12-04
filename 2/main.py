def is_report_safe(report):
    safe = True
    asc = False
    desc = False

    for i in range(len(report) - 1):
        if report[i] > report[i + 1]:
            asc = True
        else:
            desc = True

        if abs(report[i] - report[i + 1]) > 3 or (asc and desc) or (report[i] == report[i + 1]):
            safe = False
            break

    return safe


safe_reports = 0
counter = 0
reports = []
unsafe_reports = []

with open('input.txt') as input:
    for report in input.readlines():
        report = [int(x) for x in report.strip().split(' ')]
        reports.append(report)
        safe = is_report_safe(report)

        if safe:
            safe_reports += 1
        else:
            unsafe_reports.append(report)

    print(f"Sol 1: {safe_reports}")

for unsafe_report in unsafe_reports:
    for i in range(len(unsafe_report)):
        preport = unsafe_report[:i] + unsafe_report[i + 1:]
        safe = is_report_safe(preport)

        if safe:
            safe_reports += 1
            break

print(f"Sol 2: {safe_reports}")
