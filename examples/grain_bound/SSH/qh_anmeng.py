#!/usr/bin/env python
# coding=utf-8
import paramiko


class SSH_qh:
    def __init__(self):
        self.private_key = paramiko.RSAKey.from_private_key_file('../tmp/anmeng', 'net@123456')
        self.username = 'anmeng'
        self.hostname = '192.168.1.2'
        self.port = 22
        print('Hello!')

    def connect(self):
        print('----------!' + '\n' + '欢迎连接')
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port, username=self.username, pkey=self.private_key)
        print('----------!' + '\n' + '您已成功建立连接')
        return ssh


# t = SSH_qh().connect()
# sftp = t.open_sftp()
# sftp.put(r'E:\Study\pe-pp\PPE\2.txt', '/work1/anmeng_work/zkl/PPE/1.txt')
# print('上传至服务器成功')


# 执行命令
# stdin, stdout, stderr = t.exec_command('ls;cd WORK1;ls')
# # 获取命令结果
# result = stdout.read()
# print(result.decode('utf-8'))
# 关闭连接
# t.close()
