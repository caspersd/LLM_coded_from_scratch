import urllib.request

url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"

file_path = "the-verdict.txt"

resp = urllib.request.urlretrieve(url)
txt = resp.read()

