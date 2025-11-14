# 我的第一个GIS Python脚本
print("Hello GitHub and GIS!")

def calculate_area(length, width):
    """计算矩形面积"""
    return length * width

# 测试函数
if __name__ == "__main__":
    area = calculate_area(10, 5)
    print(f"矩形面积: {area}")