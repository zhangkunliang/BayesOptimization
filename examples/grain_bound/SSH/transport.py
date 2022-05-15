#!/usr/bin/env python
# -*-coding:utf-8-*-
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('../tmp/anmeng', '')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.1.2', port=22, username='anmeng', pkey=private_key)

# 文件传输
sftp = ssh.open_sftp()
# 将remove_path 下载到本地 local_path
# sftp.get(remotepath='/work1/anmeng_work/zkl/PPE/bb.py', localpath=r'E:\Study\pe-pp\PPE\2.txt')
sftp.put(localpath=r'E:\Study\pe-pp\PPE\2.txt', remotepath='/work1/anmeng_work/zkl/PPE/1.txt')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
result = stdout.read()
print(result.decode('utf-8'))
# 关闭连接
ssh.close()
