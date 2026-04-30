# ========================================
# 微环境物理场与 Agent 配置文件
# ========================================

# 物理场模拟配置
GRID_SIZE = (50, 50)       # 微环境网格尺寸 (行, 列)
DIFFUSION_RATE = 0.15      # 物理场扩散系数 (Alpha)
SOURCE_INTENSITY = 8.0     # 异常源初始释放强度

# 智能预警 Agent 配置
WARNING_THRESHOLD = 50.0   # 预警阈值：超过此值触发警告
DANGER_THRESHOLD = 80.0    # 危险阈值：超过此值触发紧急疏散
TREND_WINDOW = 5           # 趋势分析的时间窗口长度（步长）
TREND_WARNING_RATE = 5.0   # 趋势异常阈值：单位时间内的上升速率