import requests

url = "https://solver-for-captcha-with-sliding-and-rotating-objects.p.rapidapi.com/v1/captcha/solver"

payload = {
	"app_info": { "aid": "1233" },
	"host": "https://verification-va.tiktokv.com",
	"id": "6b5a543534431ea493c11d85218ab824c9582",
	"mode": "slide",
	"url1": "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/ef33808b524248fd84fcbe6375afa37c~tplv-b4yrtqhy5a-2.jpeg",
	"url2": "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/c060d38a1a464365bca15ced2a9b3f4d~tplv-b4yrtqhy5a-1.png",
	"tip_y": 54,
	"verify_id": "Verify_35513fca-180d-436f-8929-beeafbbd0cfe"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "solver-for-captcha-with-sliding-and-rotating-objects.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
