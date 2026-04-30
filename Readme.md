# **微环境物理场智能预警 Agent (MicroEnv-Agent)**

本项目实现了一个基于微环境物理场演变（如温度失控、有害气体泄漏等）的智能预警 Agent。系统通过模拟 2D 空间内的物理场扩散，并结合智能 Agent 进行实时监控、趋势分析与风险预警。

## **项目特点**

* **物理场模拟 (Physics Simulator)**：采用有限差分法计算扩散方程，模拟微环境中的动态变化。  
* **智能预警 Agent (Intelligent Agent)**：结合绝对阈值（Thresholds）与时间序列趋势（Time-Series Trends）对物理场进行综合评估。  
* **实时可视化 (Real-time Visualization)**：动态热力图展示物理场的演变过程及 Agent 的实时决策。

## **目录结构**

* config.py: 项目全局配置文件（阈值、物理参数等）  
* simulator.py: 微环境物理场演变引擎  
* agent.py: 智能预警 Agent 核心逻辑  
* main.py: 主程序，包含交互与可视化渲染  
* pack\_to\_zip.py: GitHub 打包工具

## **快速开始**

1. **安装依赖**:  
   pip install \-r requirements.txt

2. **运行模拟与预警系统**:  
   python main.py

3. **打包项目上传 GitHub**:  
   python pack\_to\_zip.py  
