#import smtp_1
import pexpect
import getpass
m_p=pexpect.spawn('python smtp_1.py')
m_p.timeout=60
m_p.expect('gmail')
m_p.sendline('sowmya.kottagalu@gmail.com')
m_p.expect('Password:')
password=getpass.getpass()
m_p.sendline('password')
m_p.expect('to')
m_p.sendline('manche.srm@gmail.com')
m_p.expect('sub')
m_p.sendline('HI')
m_p.expect('mes')
m_p.sendline('HELLO')
