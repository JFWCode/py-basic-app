import netifaces
import nmap


class LanIpScan:
    # 获取网关
    def get_gateways(self):
        return netifaces.gateways()['default'][netifaces.AF_INET][0]
        # 获取到本地网关地址，这里返回192.168.1.1

        # return dict(dict(netifaces.gateways())['default'])[2][0]
        # 不推荐使用这种方式，原因是该模块已经定义了一些常量及特定的用法

    # 获取IP
    def get_ip_lists(self, gateway):
        ip_lists = []
        for i in range(1, 256):
            ip_lists.append('{}{}'.format(gateway[:-1], i))
            # 更改网关的最后一项数据并添加到列表中
        return ip_lists
        # 返回列表['192.168.1.1',--> '192.168.1.255']

    # 查看IP地址
    def scan_ip_survial(self, ip):
        nmScan = nmap.PortScanner()
        nmScan.scan(hosts=ip, arguments='-sP')
        try:
            nmScan[ip]
            return {'ScanInfo:': nmScan[ip]}
        except:
            KeyError
            return "此IP地址无效", ip

    # 获取设备信息
    def get_all_devices(self, ip_lists):
        survial_devices = []
        for ip in ip_lists:
            scan_result = LanIpScan.scan_ip_survial(ip)
            if scan_result:
                survial_devices.append(scan_result)
                print(scan_result)
        return survial_devices


if __name__ == '__main__':
    LanIpScan = LanIpScan()
    gateway = LanIpScan.get_gateways()
    ip_lists = LanIpScan.get_ip_lists(gateway)
    LanIpScan.get_all_devices(ip_lists)
