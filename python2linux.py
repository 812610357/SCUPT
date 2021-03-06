import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
font_zh = FontProperties(
    fname="/home/zgb/ojy/simhei.ttf")  # 导入中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = np.array([
    [0.50, 0.513, 0.05, 0.023],
    [1.00, 0.561, 0.05, 0.018],
    [1.50, 0.499, 0.05, 0.026],
    [2.00, 0.369, 0.05, 0.019],
    [2.50, 0.218, 0.05, 0.025]
])

x = np.array(data[:, 0])
y = np.array(data[:, 1])
xEr = np.array(data[:, 2])
yEr = np.array(data[:, 3])
x0 = np.linspace(0, 3, 300)

y0 = np.sin(x0) / (np.sqrt(x0) + 0.5 * x0)  # 定义函数

plt.plot(x0, y0, '-',
         color=(0.90, 0, 0.07),
         linewidth=1,
         label="理论曲线")
plt.errorbar(x, y, yEr, xEr, '.',
             color=(0.27, 0.45, 0.77),
             linewidth=1,
             capsize=4,  # 误差棒端长度
             label="实验结果")
# 误差图（X，Y，Y±，X±，各种选项=对应值）

plt.axis([0, 3, 0, 0.6])
plt.xlabel("$X$(mm)")
plt.ylabel("$Y$(mm)")
plt.legend(prop=font_zh)
plt.title("$F=10$N条件下$Y$与$X$关系",
          fontproperties=font_zh,
          fontsize=16)
plt.savefig(__file__+'.svg')  # 保存图片
