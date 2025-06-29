import os
import matplotlib.pyplot as plt
import random
import datetime

charts = [
    ('Xbar-R', 'Line1', 'Xbar-R'),
    ('XR', 'Line2', 'XR'),
    ('P Chart', 'Line3', 'P'),
    ('C Chart', 'Line4', 'C'),
    ('U Chart', 'Line5', 'U'),
    ('Xbar-S', 'Line6', 'Xbar-S'),
    ('np Chart', 'Line7', 'np'),
    ('XmR', 'Line8', 'XmR'),
    ('MR', 'Line9', 'MR'),
    ('Laney P', 'Line10', 'Laney P'),
]

output_dir = os.path.join('static', 'spc_charts')
os.makedirs(output_dir, exist_ok=True)

# 假設建立日為今天
build_date = datetime.date.today()
days = 7

for cname, gname, ctype in charts:
    # 產生半年歷史資料
    history_days = 180
    history_data = [random.uniform(10, 20) for _ in range(history_days)]
    record_high = max(history_data)
    record_low = min(history_data)
    # 產生 7 天的日期與對應 rawdata
    date_list = [(build_date - datetime.timedelta(days=i)) for i in range(days-1, -1, -1)]
    data = [random.uniform(10, 20) for _ in range(days)]
    # OOC 判斷（假設 UCL=19, LCL=11）
    UCL = 19
    LCL = 11
    ooc_points = [v for v in data if v > UCL or v < LCL]
    # 判斷 OOC 是否超過半年 high/low
    status = "正常"
    if any(v > record_high for v in ooc_points):
        status = "超過半年high"
    elif any(v < record_low for v in ooc_points):
        status = "低於半年low"
    print(f"{cname}_{gname}_{ctype}: {status}")
    # 畫圖
    plt.figure(figsize=(8, 3))
    plt.plot(date_list, data, marker='o')
    plt.axhline(UCL, color='r', linestyle='--', label='UCL')
    plt.axhline(LCL, color='b', linestyle='--', label='LCL')
    plt.title(f'SPC Chart: {cname} {gname} {ctype} ({status})')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()
    filename = f'{cname}_{gname}_{ctype}.png'
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

print(f"All SPC charts saved to {output_dir}")
