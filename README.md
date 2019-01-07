# W14：[通道转换](https://github.com/OS-Q/W14)

[![sites](OS-Q/OS-Q.png)](http://www.OS-Q.com)

#### 归属桥接管道：[M4](https://github.com/OS-Q/M4)

#### 关于系统架构：[OS-Q](https://github.com/OS-Q/OS-Q)

## [平台描述](https://github.com/OS-Q/W14/wiki) 

通道转换平台,用于变换物理通信方式或通信协议,通道平台受其他设备控制

### [共用资源](https://github.com/OS-Q/W14/wiki/) 

---

- 边缘设备命名规则：体系 Q:[1,4] -> 节点 M:[1,12] -> 平台 W:[1,52] -> 设备 D:[1,365]

- naming patterns：system Q[1,4] -> node M[1,12] -> platform W[1,52] -> device D[1,365]

## [包含设备](https://github.com/OS-Q/W14/wiki) 

#### D92：[USB](https://github.com/OS-Q/D92)

将数据转换为USB通信数据，方便适配各种标准设备

#### D93：[RS485](https://github.com/OS-Q/D93)

将数据转换为RS485信号，用于长距离和控制类适配

#### D94：[Ethernet](https://github.com/OS-Q/D94)

通过以太网转发数据，实现数据入网或者长距通信

#### D95：[IR](https://github.com/OS-Q/D95)

将通信数据转换为IR信号发送，短距无线通信控制

#### D96：[ISM-HF](https://github.com/OS-Q/D96)

将数据转换为高频ISM射频信号，实现近距离通信

#### D97：[ISM-LF](https://github.com/OS-Q/D97)

将数据转换为低频ISM射频信号，实现远距离通信

#### D98：[LoRa](https://github.com/OS-Q/D98)

将数据转换为LoRa射频信号，实现广域无线通信

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
