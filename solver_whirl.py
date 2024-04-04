import requests

url = "https://solver-for-captcha-with-sliding-and-rotating-objects.p.rapidapi.com/v1/captcha/solver"

payload = {
	"app_info": { "aid": "1233" },
	"host": "https://verification-va.tiktokv.com",
	"id": "a623a0ef05cb73454343f715da018311dba2012345",
	"mode": "whirl",
	"url1": "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/d7034b39754f4af7901c028fb2ccb505~tplv-b4yrtqhy5a-2.jpeg",
	"url2": "https://p16-rc-captcha-va.ibyteimg.com/tos-maliva-i-b4yrtqhy5a-us/e37134193ebf4534a200be263cc23fdb~tplv-b4yrtqhy5a-2.jpeg",
	"verify_id": "Verify_ab7acab9-898f-465e-8b24-8f94ce721a5b"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "solver-for-captcha-with-sliding-and-rotating-objects.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
