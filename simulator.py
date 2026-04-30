import numpy as np

class MicroEnvSimulator:
    """微环境物理场（如温度、有害气体浓度）演变模拟器"""
    
    def __init__(self, grid_size, diffusion_rate):
        self.grid_size = grid_size
        self.alpha = diffusion_rate
        self.field = np.zeros(grid_size)
        self.sources = []

    def add_source(self, position, intensity):
        """添加物理场异常源 (例如：泄漏点、起火点)"""
        self.sources.append((position, intensity))

    def step(self):
        """演变一步：利用有限差分法模拟扩散和源的释放"""
        
        # 1. 施加异常源的影响
        for pos, intensity in self.sources:
            # 确保坐标在边界内
            if 0 <= pos[0] < self.grid_size[0] and 0 <= pos[1] < self.grid_size[1]:
                self.field[pos] += intensity

        # 2. 扩散方程的拉普拉斯算子计算 (Laplacian operator)
        laplacian = (
            np.roll(self.field, 1, axis=0) +
            np.roll(self.field, -1, axis=0) +
            np.roll(self.field, 1, axis=1) +
            np.roll(self.field, -1, axis=1) -
            4 * self.field
        )
        
        # 3. 处理边界条件（简单的绝热/封闭边界，边界处无通量）
        laplacian[0, :] = laplacian[-1, :] = 0
        laplacian[:, 0] = laplacian[:, -1] = 0

        # 4. 更新物理场状态
        self.field += self.alpha * laplacian
        
        # 5. 自然衰减/消散（模拟空气流通或冷却）
        self.field *= 0.985