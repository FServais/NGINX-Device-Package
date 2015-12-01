from API.Device import Device
from NginxDevice import NginxDevice
import paramiko

class NginxDeviceSSH(Device):

    __NGINX_DIR = '/etc/nginx'
    __AVAILABLE_DIR = '/sites-available'
    __ENABLED_DIR = '/sites-enabled'


    def __init__(self, device_dict):
        Device.__init__(self, device_dict)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.ssh.connect(self.host_ip, username=self.username, password=self.password)
        except paramiko.ssh_exception.BadAuthenticationType:
            print("{}{}".format("Could not connect to host ", self.host_ip))
            return False

        return True

    def get_file(self, filepath):
        ftp = self.ssh.open_sftp()

        if ftp is None:
            return

        ftp.get(filepath, 'local.txt')
        ftp.close()

    def get_stat(self):
        ftp = self.ssh.open_sftp()

        if ftp is None:
            return

        stat = ftp.stat('/etc/nginx/sites-enabled')
        ftp.close()

        return stat

    def get_site_list(self, all_available_sites=False):

        list_sites = self.ls(self.__NGINX_DIR + (self.__AVAILABLE_DIR if all_available_sites else self.__ENABLED_DIR))

        return (True, [str(site) for site in list_sites])

    def get_site_config(self, site_name):
        return self.cat(self.__NGINX_DIR + self.__AVAILABLE_DIR + '/' + site_name)

    def create_site_config(self, site_name, config, enable=True):
        self.write_file(self.__NGINX_DIR + self.__AVAILABLE_DIR + '/' + site_name, config)

        if enable:
            self.create_symb_link(self.__NGINX_DIR + self.__AVAILABLE_DIR + '/' + site_name, self.__NGINX_DIR + self.__ENABLED_DIR + '/' + site_name)

        return True

    def update_site_config(self, site_name, config, enable=True):
        return self.create_site_config(site_name, config, enable)

    # -------- Tools

    def ls(self, path):
        stdin, stdout, stderr = self.ssh.exec_command('ls ' + path)
        return [str(line).rstrip() for line in stdout.readlines()] # Remove '\n'

    def cat(self, filepath):
        stdin, stdout, stderr = self.ssh.exec_command('cat ' + filepath)
        localstring = stdout.readlines()
        return ''.join([str(line) for line in stdout.readlines()]) # Remove '\n'

    def write_file(self, filepath, content):
        stdin, stdout, stderr = self.ssh.exec_command('echo -e "' + content + '" > ' + filepath)

    def create_symb_link(self, file1, file2):
        stdin, stdout, stderr = self.ssh.exec_command('ln -s ' + file1 + ' ' + file2)

if __name__ == "__main__":
    device = {'creds': {'username': 'fservais', 'password': ''}, 'host': '127.0.0.1', 'port': 80, 'virtual': True}

    ssh_device = NginxDeviceSSH(device)
    if ssh_device.connect():
        print(ssh_device.ls("/etc/nginx/sites-available/"))
        print(ssh_device.cat("/etc/nginx/sites-available/default"))
