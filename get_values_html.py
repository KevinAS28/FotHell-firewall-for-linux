#!/usr/bin/python3

import re
html = b"""POST /run_command.html HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost/Enc_Dec.html
Cookie: hblid=Sj6tvktBo8eUrJa83m39N0IV0LGBK0o2; olfsk=olfsk4783026113382419
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=---------------------------20008043351174734977406886802
Content-Length: 709

-----------------------------20008043351174734977406886802
Content-Disposition: form-data; name="myfile"; filename="eternalblue"
Content-Type: application/octet-stream

dpkg --add-architecture i386
apt-get update
apt-get install wine
apt-get install winetricks
apt-get install wine32

/usr/share/metasploit-framework/modules/exploits/windows/smb

search eternalblue
auxiliary/scanner/smb/smb_ms17_010
show options
set rhost ...
exploit

use exploit/windo
"""
def get_values(html_var, html_data):
 try:
  html_data = html_data.decode("utf-8")
 except:
  pass
 try:
  html_var = html_var.decode("utf-8")
 except:
  pass
 rhtml_data = r"{}".format(html_data)
 rhtml_var = r"{}".format(html_var) + "="
 dapet = re.search(r"({variabel})([\w\%\*\-\_\.\+]+)".format(variabel=rhtml_var), rhtml_data)
 if dapet:
  return dapet.group(2)
 else:
  return False

def get_file(html_data):
 match = re.findall(r"(Content-Type:)(.*)(\n)".encode("utf-8"), html_data)
 return html_data[(re.search((match[1][0]+match[1][1]), html_data).span())[1]:-1]
 #and the rest is the file data

print(get_file(html))
