

import urllib
import requests
import ssl

url1 ='https://tis.sustech.edu.cn/authentication/main'

context = ssl._create_unverified_context()
urllib.request.urlopen(url1, context=context)






cookies = {
    'route': '083de9231b2c6e9b2296ecd4cf61a66e',
    'PHPSESSID': 'tb5ddflsgdl1jri8ad0qn3skq5',
    'JSESSIONID': '0198BFEF4A7A51D1DD6EB999BA7CD7C1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'route=083de9231b2c6e9b2296ecd4cf61a66e; PHPSESSID=tb5ddflsgdl1jri8ad0qn3skq5; JSESSIONID=0198BFEF4A7A51D1DD6EB999BA7CD7C1',
    'Origin': 'https://tis.sustech.edu.cn',
    'Referer': 'https://tis.sustech.edu.cn/Xsxk/query/1',
    'RoleCode': '01',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'p_pylx': '1',
    'mxpylx': '1',
    'p_sfgldjr': '0',
    'p_sfredis': '0',
    'p_sfsyxkgwc': '0',
    'p_xktjz': 'rwtjzyx',
    'p_chaxunxh': '',
    'p_gjz': '生命',
    'p_skjs': '',
    'p_xn': '2022-2023',
    'p_xq': '2',
    'p_xnxq': '2022-20232',
    'p_dqxn': '2022-2023',
    'p_dqxq': '2',
    'p_dqxnxq': '2022-20232',
    'p_xkfsdm': 'bxxk',
    'p_xiaoqu': '',
    'p_kkyx': '',
    'p_kclb': '',
    'p_xkxs': '',
    'p_id': 'ECF31649B1D9E20AE053CA0412AC40CB',
    'p_sfhlctkc': '0',
    'p_sfhllrlkc': '0',
    'p_kxsj_xqj': '',
    'p_kxsj_ksjc': '',
    'p_kxsj_jsjc': '',
    'p_kcdm_js': '',
    'p_kcdm_cxrw': '',
    'p_kc_gjz': '',
    'p_xzcxtjz_nj': '',
    'p_xzcxtjz_yx': '',
    'p_xzcxtjz_zy': '',
    'p_xzcxtjz_zyfx': '',
    'p_xzcxtjz_bj': '',
    'p_sfxsgwckb': '1',
    'p_skyy': '',
    'p_chaxunxkfsdm': '',
    'pageNum': '1',
    'pageSize': '12',
}

response = requests.post('https://tis.sustech.edu.cn/Xsxk/addGouwuche', cookies=cookies, headers=headers, data=data)


print(response.text)