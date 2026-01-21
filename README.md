### 手写数字识别应用
- 1 用Keras编写及导出预测手写数字的模型
- 2 手写字符的分割（提供两个解决思路）
- 3 特征工程（将自己的手写数字转换为MNIST数字集的模式）
- 4 用我们编写的模型预测出结果并输出（如下所示的效果）

代码中主要实现了以下几个功能，输入一张照片可以分辨出数字，并识别输出到图示中，以下是效果
<img width="684" height="437" alt="image" src="https://github.com/user-attachments/assets/3c66663e-0c06-4ea7-9a2b-a4b29fbe490d" />
<img width="677" height="385" alt="image" src="https://github.com/user-attachments/assets/cab9f30b-44c7-4c8b-89f9-3ee0051d2407" />
<img width="692" height="394" alt="image" src="https://github.com/user-attachments/assets/7127920f-5cf7-4fa0-8e1b-7bb3ae554954" />



================================== 我是分割线 =================================

### model.py
基于keras编写了预测模型并训练，保存成my_mnist_model.h5模型

### main.py
分别有以下几个模块
- 1 findBorderHistogram ---- 寻找边框，返回边框的左上角和右下角（利用直方图寻找边缘算法（需行对齐））
- 2 findBorderContours  ---- 寻找边框，返回边框的左上角和右下角（利用cv2.findContours）
- 3 transMNIST          ---- 根据边框转换为MNIST格式
- 4 predict             ---- 导入模型输出预测结果
- 5 showResults         ---- 显示结果及边框

ps. 以下是my_mnist_model.h5生成所用的模块版本号，低于此版本的可能代码加载不起来

Tensorflow  -- 1.12.0

Keras       -- 2.2.4

opencv2     -- 3.4.4


