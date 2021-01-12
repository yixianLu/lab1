import requests
#print(requests.__version__)
#r = requests.get('https://www.ualberta.ca/index.html') 
#print(r)
#r_p = requests.get('https://github.com/yixianLu/lab1/blob/main/script.py')
#r_p.content

def download_file(url):
    local_filename = url.split('/')[-1]+"_download"
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    r.close()
    return local_filename

download_file('https://github.com/yixianLu/lab1/blob/main/script.py')