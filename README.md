COMmon Bayesian Optimization Library ( COMBO )
========
Bayesian optimization has been proven as an effective tool in accelerating scientific discovery.
A standard implementation (e.g., scikit-learn), however,
can accommodate only small training data.
COMBO is highly scalable due to an efficient protocol that employs
Thompson sampling, random feature maps, one-rank Cholesky update and
automatic hyperparameter tuning. Technical features are described in [our document](/docs/combo_document.pdf).


# Required Packages ############################
* Python 2.7.x
* numpy  >=1.10
* scipy  >= 0.16
* Cython >= 0.22.1
* mpi4py >= 2.0 (optional)


# Install ######################################
	1. Download or clone the github repository, e.g.
		> git clone https://github.com/tsudalab/combo.git

	2. Run setup.py install
		> cd combo
		> python setup.py install

# Uninstall

	1. Delete all installed files, e.g.
		> python setup.py install --record file.txt
		> cat file.txt  | xargs rm -rvf


# Usage
After installation, you can launch the test suite from ['examples/grain_bound/tutorial.ipynb'](examples/grain_bound/tutorial.ipynb).

## License
This package is distributed under the MIT License.
# 一、随机搜索序列
## 1.全局序列号描述符文件生成（遍历目录文件名生成）
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202533.png)
## 2.前两次搜索采用随机的方式，每次搜索20个结构
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202601.png)
## 3.将搜索结果传入模拟函数中，再将模拟器返回的热导率值一并传入贝叶斯模型中
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202627.png)
# 二、批量提交任务
## 1.根据搜索结果，调用另外一个批量提交任务的接口，实现过程如下：
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202713.png)
# 三、计算热导率
## 1.修改Main_thermal_conductivity3.0.py，计算两个case，最后求平均
- 增加如下代码

![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202747.png)
## 2.批量运行Main_thermal_conductivity3.0.py，返回每个结构的平均热导率
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202823.png)
# 四、贝叶斯第一次训练
- 每次优化过程记录优化时间
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202855.png)
- 第一次训练耗时：114s
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202915.png)
# 五、程序整体思路
## 1.加载描述符文件
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515202938.png)
## 2.新建结构文件及时间日志文件
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515203000.png)
## 3.将模拟器类属性值初始化为out文件中的格式，仅存入第一列，并全部置为0，后续位置上有值再进行原地修改
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515203020.png)
## 4.贝叶斯搜索结构序列号索引值
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515203039.png)
## 5.将搜索值存入input_Descriptor中
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515203114.png)
## 6.将热导率序列按序保存到self.t矩阵中
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515203128.png)
## 7.保存更新后的输出矩阵，并返回更改位置的热导率值，并传入policy中
![](https://xingqiu-tuchuang-1256524210.cos.ap-shanghai.myqcloud.com/674/20220515203143.png)
