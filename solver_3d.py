import requests

url = "https://solver-for-captcha-with-sliding-and-rotating-objects.p.rapidapi.com/v1/captcha/solver"

payload = {
	"app_info": { "aid": "1233" },
	"host": "https://verification-va.tiktokv.com",
	"id": "5e1acc8649695d9bsadd34543sasdsdsfe4ff48b50",
	"mode": "3d",
	"url1": "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/3d_2385_0ca2bd260ef09671ad4a316c223b911e9c6847a2_1.jpg~tplv-b4yrtqhy5a-2.jpeg",
	"verify_id": "Verify_90c4fae2-31dc-4656-9011-28e738efb43c"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "solver-for-captcha-with-sliding-and-rotating-objects.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
