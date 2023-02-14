import requests

cookies = {
    'HMACCOUNT_BFESS': '82F595A98702508C',
    'BDUSS_BFESS': 'E50ZGptQ3VXdFVEd3ZnZzExNTdGeHhzLXhiejlEWVlPM0J0RFk0eVhpTDFXZkJqSVFBQUFBJCQAAAAAAAAAAAEAAAC5jkmC0Ka1veKny8C1xLzSu-8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXMyGP1zMhjb',
    'ab_sr': '1.0.1_ZTI1MDQzOWUxMzc0YmM3YzY4ZjQxOGRjNzI2OGU2NGJjMjFkNGY4OGI5NTNkMzU5NGYwMWRmOTZmNzRlZGVlMDBiOGFjZTdkNjQ3YmRkYzg2ODM1NjBhYzMwOGViZDUwNTVhNzUwZTI0YzIwODg1NTYyOTVlMTZhMDE5ZWQyNGI0OWZkNWRhNTM4ZjJlNTE4M2UxMDNiM2QzZDk2Y2QzMmUwZDU5NmUxNTU2Y2QyNWNmNmRjY2IyYzBhYWQxY2Q3',
    'BAIDUID_BFESS': '83BE332FF830492D55B31153B839F74C:FG=1',
}

headers = {
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'HMACCOUNT_BFESS=82F595A98702508C; BDUSS_BFESS=E50ZGptQ3VXdFVEd3ZnZzExNTdGeHhzLXhiejlEWVlPM0J0RFk0eVhpTDFXZkJqSVFBQUFBJCQAAAAAAAAAAAEAAAC5jkmC0Ka1veKny8C1xLzSu-8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPXMyGP1zMhjb; ab_sr=1.0.1_ZTI1MDQzOWUxMzc0YmM3YzY4ZjQxOGRjNzI2OGU2NGJjMjFkNGY4OGI5NTNkMzU5NGYwMWRmOTZmNzRlZGVlMDBiOGFjZTdkNjQ3YmRkYzg2ODM1NjBhYzMwOGViZDUwNTVhNzUwZTI0YzIwODg1NTYyOTVlMTZhMDE5ZWQyNGI0OWZkNWRhNTM4ZjJlNTE4M2UxMDNiM2QzZDk2Y2QzMmUwZDU5NmUxNTU2Y2QyNWNmNmRjY2IyYzBhYWQxY2Q3; BAIDUID_BFESS=83BE332FF830492D55B31153B839F74C:FG=1',
    'Referer': 'https://blog.csdn.net/john_bian/article/details/68059250',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get(
    'https://hm.baidu.com/hm.gif?hca=82F595A98702508C&cc=1&ck=1&cl=24-bit&ds=1260x840&vl=721&ep=5079%2C3804&et=10&ja=0&ln=zh-cn&lo=0&lt=1676117229&rnd=1010737561&si=6bcd52f51e9b3dce32bec4a3997715ac&su=https%3A%2F%2Fcn.bing.com%2F&v=1.3.0&lv=3&sn=20389&r=0&ww=1004&p=islogin*1*1!isonline*1*1!isvip*0*1!uid_*NGC2238*1!view_h_*721&u=https%3A%2F%2Fblog.csdn.net%2Fjohn_bian%2Farticle%2Fdetails%2F68059250',
    cookies=cookies,
    headers=headers,
)
print(response.text)