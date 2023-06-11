# 导入time模块
import time

# 定义一个秒表类
class Stopwatch:

    # 初始化方法，设置开始时间和结束时间为None
    def __init__(self):
        self.start_time = None
        self.end_time = None

    # 开始计时的方法，记录当前时间为开始时间
    def start(self):
        self.start_time = time.time()

    # 停止计时的方法，记录当前时间为结束时间
    def stop(self):
        self.end_time = time.time()

    # 获取经过的时间的方法，返回结束时间减去开始时间的差值，单位为秒
    def get_elapsed_time(self):
        return self.end_time - self.start_time

# 创建一个秒表对象
stopwatch = Stopwatch()

# 调用开始计时的方法
stopwatch.start()

# 做一些操作，比如打印一些内容
print("Hello, this is Bing.")

# 调用停止计时的方法
stopwatch.stop()

# 调用获取经过的时间的方法，并打印结果
print("Elapsed time:", stopwatch.get_elapsed_time(), "seconds")
