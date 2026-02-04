# 简单测试版本
daily = 200
per_day_get_bonus = 10
bonus = 1000

def calculate_income(days):
    total = 0
    for day in range(1, days + 1):
        today_bonus = bonus if day % per_day_get_bonus == 0 else 0
        total += daily + today_bonus
    return total

print("工作天数 vs 总收入分析")
print("=" * 40)
days = 0
for days in range (1, 30+1):
    income = calculate_income(days)
    avg = income / days
    bonus_count = days // per_day_get_bonus
    print(f"{days:2d}天: 总收入={income:5.0f}元, 日均={avg:6.2f}元, 奖金次数={bonus_count}次")

print(f"{days:2d}天详细计算:")

total = calculate_income(days)
print(f"{days}天总收入: {days}元")
print(f"基础工资: {days * daily}元")
print(f"奖金总数: {(days// per_day_get_bonus) * bonus}元")
print(f"奖金次数: {days // per_day_get_bonus}次")
print(f"总收入是 {total} 元")
