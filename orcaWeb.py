import requests
url = 'http://10.104.128.12:8080/orca_web/edits/editlist.jsp?line=NN54_S21B1240A130&groups=-1'
username = "qc_online"
password = "qc_online"
import requests

# Fill in your details here to be posted to the login form.
payload = {
    'username': username,
    'password': password
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post("http://10.104.128.12:8080/orca_web/main.jsp", data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)

    # An authorised request.
