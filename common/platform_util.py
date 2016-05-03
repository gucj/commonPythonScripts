# coding=utf-8
__author__ = "gucuijuan"
import platform
platform.platform()  # 获取操作系统名称及版本号，'Darwin-15.0.0-x86_64-i386-64bit'
platform.version()  # 获取操作系统版本号,'6.1.7601'
platform.architecture()  # 获取操作系统的位数,('64bit', '')
platform.machine()  # 计算机类型,'x86_64'
platform.node()  # 计算机的网络名称，'XXXXXMacBook-Pro.local'
platform.processor()  # 计算机处理器信息，''i386''
platform.uname()  # 包含上面所有的信息汇总,('Darwin', 'MacBook-Pro.local', '15.0.0', 'Darwin Kernel Version 15.0.0: Sat Sep 19 15:53:46 PDT 2015; root:xnu-3247.10.11~1/RELEASE_X86_64', 'x86_64', 'i386')
