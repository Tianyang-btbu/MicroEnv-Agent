import numpy as np
from datetime import datetime

class IntelligentWarningAgent:
    """基于物理场演变的智能预警 Agent"""
    
    def __init__(self, warning_threshold, danger_threshold, trend_window, trend_warning_rate):
        self.warning_threshold = warning_threshold
        self.danger_threshold = danger_threshold
        self.trend_window = trend_window
        self.trend_warning_rate = trend_warning_rate
        
        # 用于保存环境演变的短期记忆
        self.history_max = []
        self.history_mean = []

    def analyze(self, field_state, time_step):
        """分析当前物理场状态并生成智能决策报告"""
        
        current_max = np.max(field_state)
        current_mean = np.mean(field_state)

        # 记录记忆
        self.history_max.append(current_max)
        self.history_mean.append(current_mean)

        risk_level = "NORMAL"  # 正常状态
        suggestion = "环境参数正常，持续监控中。"

        # 1. 基于绝对阈值的危险研判
        if current_max >= self.danger_threshold:
            risk_level = "DANGER"
            suggestion = "检测到极高异常值！请立即启动应急预案并疏散相关区域人员！"
        elif current_max >= self.warning_threshold:
            risk_level = "WARNING"
            suggestion = "环境参数超标，请尽快派安保或技术人员前往现场核查异常源。"

        # 2. 基于时间序列演变趋势的智能预测 (Trend Analysis)
        trend_rate = 0.0
        if len(self.history_max) > self.trend_window:
            past_max = self.history_max[-self.trend_window]
            trend_rate = (current_max - past_max) / self.trend_window
            
            # 如果当前值未触碰红线，但是上升趋势极其猛烈，则提前发出预警
            if trend_rate > self.trend_warning_rate and risk_level == "NORMAL":
                risk_level = "WARNING"
                suggestion = f"智能预测触发：虽然当前绝对值未超标，但检测到异常的急剧上升趋势 (增速: {trend_rate:.2f}/步)，请密切关注潜在爆发风险。"

        # 生成并返回结构化预警报告
        report = {
            "time_step": time_step,
            "max_value": round(current_max, 2),
            "mean_value": round(current_mean, 2),
            "trend_rate": round(trend_rate, 2),
            "risk_level": risk_level,
            "suggestion": suggestion,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        return report