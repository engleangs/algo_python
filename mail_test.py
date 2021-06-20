import subprocess


def mail(from_addr, to_addr, subject='Testing', body='Hello'):
    cmd = 'echo ' + body + ' | mail -s ' + subject + ' -r ' + from_addr + ' ' + to_addr
    send = subprocess.call(cmd, shell=True)
    return send


if __name__ == "__main__":
    mail("sam.engleang@asiacell.com", "sam.engleang@asiacell.com")
