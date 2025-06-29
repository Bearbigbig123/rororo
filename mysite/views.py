import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse
def get_spc_chart_img(request):
    cname = request.GET.get('cname')
    gname = request.GET.get('gname')
    ctype = request.GET.get('ctype')
    # 模擬 rawdata
    rawdata = [round(random.uniform(10, 20), 2) for _ in range(20)]
    plt.figure(figsize=(6, 3))
    plt.plot(rawdata, marker='o')
    plt.title(f'SPC Chart: {cname} {gname} {ctype}')
    plt.xlabel('Sample')
    plt.ylabel('Value')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type='image/png')
import random
from django.http import JsonResponse
def get_spc_chart(request):
    cname = request.GET.get('cname')
    gname = request.GET.get('gname')
    ctype = request.GET.get('ctype')
    # 模擬 rawdata
    rawdata = [round(random.uniform(10, 20), 2) for _ in range(20)]
    # 模擬圖片網址
    chart_url = f"/static/spc_charts/{cname}_{gname}_{ctype}.png"
    return JsonResponse({
        'cname': cname,
        'gname': gname,
        'ctype': ctype,
        'rawdata': rawdata,
        'chart_url': chart_url
    })
from django.shortcuts import render
from datetime import datetime

def rollback_task_detail(request):
    # 模擬每一筆的 ooc_record_status
    task_list = [
        {
            'cname': 'Xbar-R', 'gname': 'Line1', 'ctype': 'Xbar-R', 'trend_chart': 'Xbar-R_Line1_Xbar-R.png', 'reason': '點超出UCL', 'ooc_record_status': '正常'
        },
        {
            'cname': 'XR', 'gname': 'Line2', 'ctype': 'XR', 'trend_chart': 'XR_Line2_XR.png', 'reason': '連續7點上升', 'ooc_record_status': '超過半年high'
        },
        {
            'cname': 'P Chart', 'gname': 'Line3', 'ctype': 'P', 'trend_chart': 'P Chart_Line3_P.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
        {
            'cname': 'C Chart', 'gname': 'Line4', 'ctype': 'C', 'trend_chart': 'C Chart_Line4_C.png', 'reason': 'None', 'ooc_record_status': '低於半年low'
        },
        {
            'cname': 'U Chart', 'gname': 'Line5', 'ctype': 'U', 'trend_chart': 'U Chart_Line5_U.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
        {
            'cname': 'Xbar-S', 'gname': 'Line6', 'ctype': 'Xbar-S', 'trend_chart': 'Xbar-S_Line6_Xbar-S.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
        {
            'cname': 'np Chart', 'gname': 'Line7', 'ctype': 'np', 'trend_chart': 'np Chart_Line7_np.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
        {
            'cname': 'XmR', 'gname': 'Line8', 'ctype': 'XmR', 'trend_chart': 'XmR_Line8_XmR.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
        {
            'cname': 'MR', 'gname': 'Line9', 'ctype': 'MR', 'trend_chart': 'MR_Line9_MR.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
        {
            'cname': 'Laney P', 'gname': 'Line10', 'ctype': 'Laney P', 'trend_chart': 'Laney P_Line10_Laney P.png', 'reason': 'None', 'ooc_record_status': '正常'
        },
    ]
    context = {
        'task': {
            'title': 'F18A - Rollback_CHI Task',
            'status': '已通過',
            'applicant': 'KJ (EMPE866673596)',
            'fab': 'F18A',
            'create_time': datetime(2025, 6, 27, 15, 31),
            'task_type': 'Rollback_CHI',
            'expire': 'within_3month',
            'tasks': task_list
        }
    }
    return render(request, 'rollback_detail.html', context)
