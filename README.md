# W14：[通道转换](https://github.com/OS-Q/W14)

[![sites](OS-Q/OS-Q.png)](http://www.OS-Q.com)

#### 归属桥接管道：[M4](https://github.com/OS-Q/M4)

#### 关于系统架构：[OS-Q](https://github.com/OS-Q/OS-Q)

## [平台描述](https://github.com/OS-Q/W14/wiki) 

通道转换平台,用于变换物理通信方式或通信协议,平台受其他设备控制

### [共用资源](https://github.com/OS-Q/W14/wiki/) 

---

- 边缘设备命名规则：体系 Q:[1,4] -> 节点 M:[1,12] -> 平台 W:[1,52] -> 设备 D:[1,365]

- naming patterns：system Q[1,4] -> node M[1,12] -> platform W[1,52] -> device D[1,365]

## [包含设备](https://github.com/OS-Q/W14/wiki) 

#### D92：[RS485](https://github.com/OS-Q/D92)

将串口通信数据转换为RS485信号发送

#### D93：[USB](https://github.com/OS-Q/D93)

将串口通信数据转换为USB数据发送

#### D94：[Ethernet](https://github.com/OS-Q/D94)

通过串口或SPI接收转发数据通过以太网发送数据

#### D95：[IR](https://github.com/OS-Q/D95)

将通信数据转换为IR信号发送

#### D96：[ISM-LF](https://github.com/OS-Q/D96)

通过射频芯片将数据信号转换为433MHz频段无线电发送

#### D97：[ISM-HF](https://github.com/OS-Q/D97)

将通信数据转换为2.4GHz频段射频发送出去

#### D98：[LORA](https://github.com/OS-Q/D98)

将通信数据转换为LORA发送

## [同级平台](https://github.com/OS-Q/M4/wiki)

#### -> W14：[通道转换](https://github.com/OS-Q/W14)

物理通信通道或通信协议的改变

#### W15：[通道扩展](https://github.com/OS-Q/W15)

通信通道数量和适配的种类扩充

#### W16：[通信中继](https://github.com/OS-Q/W16)

通信信号在传输过程中进行补强

#### W17：[专用模块](https://github.com/OS-Q/W17)

用于适配他人设备专用桥接模块

---

####  © qitas@qitas.cn
###  [OS-Q redefined Operation System](http://www.OS-Q.com)
####  @ 2019-1-3
