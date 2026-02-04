import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 每日工资x + 每d天, 有b奖金。
daily = input("你每天的收入是: ")
daily = int(daily)
per_day_get_bonus = input("你每工作[？]天就可以拿到奖金")
per_day_get_bonus = int(per_day_get_bonus)
bonus = input("奖金是: ")
bonus = int(bonus)

plt.rcParams["font.sans-serif"] = ["SimHei"]   # 黑体
plt.rcParams["axes.unicode_minus"] = False

def calculate_income_for_days(work_days):
    """计算指定工作天数的总收入"""
    records = []
    total_sum = 0
    
    for day in range(1, work_days + 1):
        today_bonus = bonus if day % per_day_get_bonus == 0 else 0
        today_income = daily + today_bonus
        total_sum = total_sum + today_income
        
        records.append({
            "Day": day,
            "Daily Salary": daily,
            "Bonus": today_bonus,
            "Today Income": today_income,
            "Total Income": total_sum
        })
    
    return pd.DataFrame(records), total_sum

# 计算不同工作天数的影响
day_range = range(1, 31)  # 1-30天
income_results = []

for days in day_range:
    _, total_income = calculate_income_for_days(days)
    income_results.append({
        "Work Days": days,
        "Total Income": total_income,
        "Daily Average": total_income / days,
        "Bonus Count": days // per_day_get_bonus,
        "Total Bonus": (days // per_day_get_bonus) * bonus
    })

# 创建结果DataFrame
results_df = pd.DataFrame(income_results)

# 显示详细结果表格
print("=" * 60)
print("不同工作天数对月收入的影响分析")
print("=" * 60)
print(results_df.to_string(index=False))

# 生成图表
plt.figure(figsize=(15, 10))

# 子图1: 总收入与工作天数关系
plt.subplot(2, 2, 1)
plt.plot(results_df["Work Days"], results_df["Total Income"], 'b-', linewidth=2, marker='o', markersize=4)
plt.xlabel('工作天数')
plt.ylabel('总收入 (元)')
plt.title('工作天数 vs 总收入')
plt.grid(True, alpha=0.4)

# 子图2: 日平均收入与工作天数关系
plt.subplot(2, 2, 2)
plt.plot(results_df["Work Days"], results_df["Daily Average"], 'g-', linewidth=2, marker='s', markersize=4)
plt.xlabel('工作天数')
plt.ylabel('日平均收入 (元)')
plt.title('工作天数 vs 日平均收入')
plt.grid(True, alpha=0.3)

# 子图3: 奖金次数与工作天数关系
plt.subplot(2, 2, 3)
plt.bar(results_df["Work Days"], results_df["Bonus Count"], color='orange', alpha=0.7)
plt.xlabel('工作天数')
plt.ylabel('获得奖金次数')
plt.title('工作天数 vs 奖金获得次数')
plt.grid(True, alpha=0.3)

# 子图4: 总奖金与工作天数关系
plt.subplot(2, 2, 4)
plt.plot(results_df["Work Days"], results_df["Total Bonus"], 'r-', linewidth=2, marker='^', markersize=4)
plt.xlabel('工作天数')
plt.ylabel('总奖金 (元)')
plt.title('工作天数 vs 总奖金')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('salary_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# 生成关键统计信息
print("\n" + "=" * 60)
print("关键统计信息")
print("=" * 60)
print(f"最低收入 (1天): {results_df['Total Income'].min():.0f} 元")
print(f"最高收入 (30天): {results_df['Total Income'].max():.0f} 元")
print(f"收入差距: {results_df['Total Income'].max() - results_df['Total Income'].min():.0f} 元")
print(f"日平均收入范围: {results_df['Daily Average'].min():.2f} - {results_df['Daily Average'].max():.2f} 元")

# 找出最佳奖金效率的工作天数
results_df['Bonus Efficiency'] = results_df['Total Bonus'] / results_df['Work Days']
best_efficiency_days = results_df.loc[results_df['Bonus Efficiency'].idxmax(), 'Work Days']
print(f"奖金效率最高的工作天数: {best_efficiency_days} 天")

# 显示30天工作的详细分解
print("\n" + "=" * 60)
print("30天工作详细收入分解")
print("=" * 60)
detailed_df, _ = calculate_income_for_days(30)
print(detailed_df.tail(10).to_string(index=False))