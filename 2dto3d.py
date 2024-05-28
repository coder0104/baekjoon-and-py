import torch
import torchvision.transforms as transforms
import cv2
import numpy as np
import open3d as o3d
from PIL import Image

# MiDaS 모델 로드
model_type = "DPT_Large"     # MiDaS 모델 유형: "DPT_Large" or "DPT_Hybrid"
midas = torch.hub.load("intel-isl/MiDaS", model_type)

# 모델을 평가 모드로 설정
midas.eval()

# 모델 변환 로드
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

# 이미지 로드
img = Image.open("sf.png").convert("RGB")

# 이미지 변환
img = np.array(img) / 255.0
img = torch.tensor(img, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0)
input_batch = img.to("cuda" if torch.cuda.is_available() else "cpu")

# 깊이 추정
with torch.no_grad():
    prediction = midas(input_batch)

# 깊이 맵 후처리
prediction = torch.nn.functional.interpolate(
    prediction.unsqueeze(1),
    size=img.shape[2:],  # 이미지 사이즈로 조정
    mode="bicubic",
    align_corners=False,
).squeeze()

depth_map = prediction.cpu().numpy()

# 이미지와 깊이 맵을 사용하여 3D 포인트 클라우드 생성
def create_point_cloud(rgb_image, depth_map):
    h, w = depth_map.shape
    i, j = np.meshgrid(np.arange(w), np.arange(h), indexing='xy')
    
    valid = depth_map > 0
    z = depth_map[valid]
    x = (i[valid] - w / 2) * z / w
    y = (j[valid] - h / 2) * z / h
    
    points = np.stack((x, y, z), axis=-1)
    colors = rgb_image[valid]
    
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.colors = o3d.utility.Vector3dVector(colors / 255.0)
    
    return point_cloud

# OpenCV를 사용하여 RGB 이미지 로드
rgb_image = cv2.cvtColor(cv2.imread("sf.png"), cv2.COLOR_BGR2RGB)

# 포인트 클라우드 생성
point_cloud = create_point_cloud(rgb_image, depth_map)

# 포인트 클라우드 시각화
o3d.visualization.draw_geometries([point_cloud])
 