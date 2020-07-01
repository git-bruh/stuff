from multiprocessing.pool import ThreadPool
import tempfile
import requests
import shutil
import glob
import sys
import os

if not os.geteuid() == 0:
    sys.exit("Script Must Be Run With Root Privileges!")

hosts_file = "/etc/hosts"
original_ip = "0.0.0.0"
destination_ip = "127.0.0.1"
source_file = "sources.txt"
header = '''
127.0.0.1   localhost
::1         localhost
'''
tempdir = tempfile.mkdtemp(dir=tempfile.gettempdir()) + "/"
merged_file = tempfile.NamedTemporaryFile(prefix=tempdir).name


def download(url):
    file = tempfile.NamedTemporaryFile(prefix=tempdir).name
    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        with open(file, "wb") as f:
            for data in r:
                f.write(data)
    return url


def merge_files(file):
    read_files = glob.glob(file)
    with open(merged_file, "wb") as merged:
        for data in read_files:
            with open(data, "rb") as data:
                merged.write(data.read())


def remove_comments(file):
    f = open(file, "r")
    output = ""
    content = f.readlines()
    for line in content:
        line = line.split("#")
        if len(line) > 1:
            line[0] += "\n"
        if line[0].rstrip():
            output += line[0]
    output = [content for content in output.split("\n") if content != ""]
    return output


def process_file(file):
    file_read = open(file, "r")
    contents = file_read.readlines()
    file_write = open(file, "w")
    for line in contents:
        line = line.replace(original_ip, destination_ip).split("#")
        if len(line) > 1:
            line[0] += "\n"
        if line[0].rstrip():
            if destination_ip not in line[0]:
                line[0] = destination_ip + " " + line[0]
            file_write.write(line[0])
    with open(file, "r") as f:
        contents = set(f.readlines())
        file = open(file, "w")
        for content in contents:
            file.write(content)


urls = remove_comments(source_file)
commented_urls = "\n".join(["# " + url for url in urls])

print("Downloading Files...")
download = ThreadPool(5).imap_unordered(download, urls)
for download in download:
    print(download)

print("Merging Files...")
merge_files(tempdir + "*")
process_file(merged_file)

with open(merged_file, "r") as f:
    blocklist = f.read()
    blocked_domains = len(blocklist.rstrip().split("\n"))
    f.close()

content = f'''
# Hosts File Generated From The Following Sources :
{commented_urls}
{header}
# Blocklist
{blocklist}
'''

print("Writing To Hosts File...")
with open(hosts_file, "w") as f:
    f.write(content)

print(f"Blocked {blocked_domains} Domains")
print("Cleaning Up...")
shutil.rmtree(tempdir)
