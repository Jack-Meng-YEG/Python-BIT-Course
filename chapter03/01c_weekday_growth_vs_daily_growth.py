"""
Problem: Investment Growth with Weekday / Weekend Variation

You manage an investment account that starts with a value of 1.0.
Each year has 365 days.

Scenario A (reference case):
- The account grows by 1% every single day (including weekends).
- After 365 days, the final value becomes approximately 37.78.

Scenario B (what we need to figure out):
- On weekdays (Monday to Friday), the account grows by an unknown daily growth rate x.
- On weekends (Saturday and Sunday), the account loses 1% per day.

Question:
What weekday growth rate x is required so that, after 365 days,
the final value in Scenario B matches the final value in Scenario A (≈ 37.78)?
"""

# weekday_growth_vs_daily_growth.py
def account_growth(weekday_rate):
    value=1.0
    for i in range(365):
        if i%7 in [6,0]:
            value=value*(1-0.01)
        else:
            value=value*(1+weekday_rate)
    return value
    
target_value=pow(1+0.01,365)
rate=0.01

while account_growth(rate)<target_value:
    rate=rate+0.001
print("Required weekday growth rate is:{:.3f}".format(rate))
print("Target final value is:{:.2f}".format(target_value))