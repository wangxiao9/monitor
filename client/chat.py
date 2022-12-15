# __author:EstherWang
# time:25/02/2021
import matplotlib.pyplot as plt
import time

from client.cpu import CPUStatus

#plt.rcParams['font.sans-serif'] = ['SimHei']

plt.ion()

plt.figure(figsize=(10,10))

cpu = []
times = []
while True:
    t = time.strftime("%H:%M:%S", time.localtime()) # 获取时间
    cpu_pre = CPUStatus().process_cpu_precent()
    cpu.append(cpu_pre)
    times.append(t)

    plt.plot(times, cpu, label='CPU_PRECENT', color="b")
    plt.ylabel('oneDirverCPU', fontsize=14)
    plt.xticks(rotation=30, fontsize=8)
    plt.yticks(range(0, 110, 10))
    plt.pause(5)

    plt.ioff()
    plt.show()