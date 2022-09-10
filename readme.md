# RaspberryPie垃圾识别
参考链接
> https://www.bilibili.com/video/BV1XT4y1J73P?spm_id_from=333.880.my_history.page.click&vd_source=8d8c1eaf1204e15d0c00cdfcaf44e70a
> https://aidoc.jd.com/image/garbageClassification.html

bilibili上代码版本太老，接口名字都变了， 已参数安装新的官方文档更新
<img src="https://ressmatthew-picture-cloud-storage.oss-cn-hangzhou.aliyuncs.com/img/image-20220813000414527.png" alt="image-20220813000414527" style="zoom:50%;" />

参数：

* timestamp 13位
* sign hashlib.md5((secretKey + str(timestamp)).encode()).hexdigest()
