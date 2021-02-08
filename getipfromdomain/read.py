import socket
import re
# Using readlines()
file1 = open('domains.txt', 'r')
file2 = open('domainips.txt', 'w')
Lines = file1.readlines()

count = 0
# Strips the newline character
COMMA_MATCHER = re.compile(r"\"|[\",]")

for line in Lines:
    domain=COMMA_MATCHER.split(line)[1]
    ip = socket.gethostbyname(domain)
    file2.write("{}\n".format(ip))
