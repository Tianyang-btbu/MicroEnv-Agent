import matplotlib.pyplot as plt
import os
import time

import config
from simulator import MicroEnvSimulator
from agent import IntelligentWarningAgent

def main():
    print("=== 启动基于微环境物理场演变的智能预警系统 ===")
    
    # 1. 初始化微环境物理场模拟器
    sim = MicroEnvSimulator(grid_size=config.GRID_SIZE, diffusion_rate=config.DIFFUSION_RATE)
    
    # 初始添加一个不易察觉的微小异常源
    sim.add_source((25, 25), config.SOURCE_INTENSITY * 0.1)

    # 2. 初始化智能预警 Agent
    agent = IntelligentWarningAgent(
        warning_threshold=config.WARNING_THRESHOLD,
        danger_threshold=config.DANGER_THRESHOLD,
        trend_window=config.TREND_WINDOW,
        trend_warning_rate=config.TREND_WARNING_RATE
    )

    # 3. 准备可视化界面
    os.makedirs("output", exist_ok=True)
    plt.ion()  # 开启交互模式
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 初始化图像数据对象，后续只更新数据以提高渲染性能
    cax = ax.imshow(sim.field, cmap='hot', interpolation='nearest', vmin=0, vmax=100)
    fig.colorbar(cax, ax=ax, label='物理场强度 (Field Intensity)')

    # 开始演变循环
    for step in range(1, 151):
        # 模拟突发事件：在第 40 步时，某处发生严重泄漏/热失控
        if step == 40:
            sim.add_source((15, 35), config.SOURCE_INTENSITY * 1.5)
            print(f"\n[环境事件] Step {step}: 坐标(15, 35)处发生突发严重异常！")

        # 模拟器演进
        sim.step()
        current_field = sim.field.copy()

        # Agent 进行智能分析
        report = agent.analyze(current_field, step)

        # 终端日志打印逻辑 (仅打印状态改变或定期报告)
        if report['risk_level'] != "NORMAL" or step % 20 == 0:
            color_code = "\033[91m" if report['risk_level'] == "DANGER" else "\033[93m" if report['risk_level'] == "WARNING" else "\033[92m"
            reset_code = "\033[0m"
            print(f"[{report['timestamp']}] Step {step:03d} | "
                  f"风险: {color_code}{report['risk_level']}{reset_code} | "
                  f"峰值: {report['max_value']} | "
                  f"建议: {report['suggestion']}")

        # 动态更新可视化画面
        cax.set_data(current_field)
        ax.set_title(f"微环境物理场实时演变 - Step {step}\n"
                     f"Agent研判等级: {report['risk_level']} | 场域最高值: {report['max_value']}")
        
        plt.pause(0.05) # 控制演变播放速度

    # 循环结束，保存并展示最终状态
    plt.ioff()
    plt.savefig("output/final_state.png")
    print("\n=== 演变模拟结束，最终状态图像已保存至 output/final_state.png ===")
    plt.show()

if __name__ == "__main__":
    main()