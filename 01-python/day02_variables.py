
# Python Lesson 2: Variables and calculations

name = "Michael"
weekly_study_hours = 10
monthly_income_target = 2000
customers = 3
monthly_fee = 400

monthly_revenue = customers * monthly_fee
annual_study_hours = weekly_study_hours * 52
income_gap = max(monthly_income_target - monthly_revenue, 0)

print("Name:", name)
print("Annual study hours:", annual_study_hours)
print("Monthly revenue: $", monthly_revenue)
print("Remaining income target: $", income_gap)
