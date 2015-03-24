# 利用arduino与BMP180传感器获取温度与气压数据并上传到电脑上
### 0. 准备材料
* arduino一台(Uno 或者 Nano)
* BMP180传感器一块
* 一些连接线
 ![image](https://github.com/qzane/eta/blob/master/1/pic/BMP180.jpg "BMP180")
 
### 1.焊接传感器上的接口
 ![image](https://github.com/qzane/eta/blob/master/1/pic/P50324-124204.jpg)
 
### 2.将传感器与arduino连接起来
* 确定arduino串口通讯使用的引脚(A4与A5)
 ![image](https://github.com/qzane/eta/blob/master/1/pic/p1.png)
 
* 连接方法如下<br>
    arduino   BMP180
    5V  ----- VIN<br>
    GND ----- GND<br>
    A5  ----- SCL<br>
    A4  ----- SDA
 ![image](https://github.com/qzane/eta/blob/master/1/pic/P50324-181950.jpg)
 
### 3.程序下载与调试
* 将arduino与电脑连接
* 打开bmp180.ino文件
 ![image](https://github.com/qzane/eta/blob/master/1/pic/p1.png)
 
* 烧录程序
 ![image](https://github.com/qzane/eta/blob/master/1/pic/p3.png)
 
* 使用Serial Monitor测试运行情况
 ![image](https://github.com/qzane/eta/blob/master/1/pic/p4.png)
 ![image](https://github.com/qzane/eta/blob/master/1/pic/p5.png)
 
 
 
