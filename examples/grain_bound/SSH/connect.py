#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko


class SshClass:
    """
    ssh连接对象
    本对象提供了密钥连接、密码连接、命令执行、关闭连接
    """
    ip = '192.168.1.2'
    port = 22
    username = 'anmeng'
    password = 'net@123456'
    timeout = 0
    ssh = None

    def __init__(self, ip, username, port=22, timeout=30):
        """
        初始化ssh对象
        :param ip: str  主机IP
        :param username: str  登录用户名
        :param port: int  ssh端口
        :param timeout: int  连接超时
        """
        self.ip = ip
        self.username = username
        self.port = port
        self.timeout = timeout
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh = ssh

    def conn_by_key(self, key):
        """
        密钥连接
        :param key: str  rsa密钥路径
        :return: ssh连接对象
        """
        rsa_key = paramiko.RSAKey.from_private_key_file(key, 'net@123456')
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, pkey=rsa_key, timeout=self.timeout)
        if self.ssh:
            return self.ssh
        else:
            self.close()
            raise Exception("密钥连接失败.")

    def conn_by_pwd(self, pwd):
        """
        密码连接
        :param pwd: str  登录密码
        :return: ssh连接对象
        """
        self.ssh.connect(hostname=self.ip, port=self.port, username=self.username, password=pwd)
        if self.ssh:
            return self.ssh
        else:
            self.close()
            raise Exception("密码连接失败.")

    def exec_command(self, command):
        """
        命令控制
        :param command: str  命令
        :return: dict  命令执行的返回结果
        """
        stdin, stdout, stderr = self.ssh_client.exec_command(commands, timeout=0, get_pty=True)
        res, err = stdout.read(), stderr.read()
        results = res if res else err
        return results.decode()

    def close(self):
        """
        关闭当前连接
        :return:
        """
        if self.ssh:
            self.ssh.close()
        else:
            raise Exception("ssh关闭失败，当前对象并没有ssh连接.")


if __name__ == '__main__':
    r_key = 'C:\Users\Administrator\AppData\Roaming\SSH\HostKeys\\anmeng'
    SSH = SshClass("192.168.1.2", "anmeng")
    ssh = SSH.conn_by_key(r_key)
    # 获取Transport实例
    tran = paramiko.Transport('192.168.1.2', 22)
    # 连接SSH服务端，使用password
    tran.connect(username='anmeng', password='net@123456')
    # 获取SFTP实例
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 设置上传的本地/远程文件路径
    localpath = "E:\Study\pe-pp\PPE"
    remotepath = "/work1/anmeng_work/zkl/PPE/aa.py"
    # 执行上传动作
    sftp.put(localpath, remotepath)
    # # 关闭连接
    # tran.close()

    # commands = 'cd WORK1/zkl;ls'
    # stdin, stdout, stderr = ssh.exec_command(commands)
    # # 获取命令结果
    # res, err = stdout.read(), stderr.read()
    # result = res if res else err
    # # 将字节类型 转换为 字符串类型
    # result = str(result)
    # print(result)
