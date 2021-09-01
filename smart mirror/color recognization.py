# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 색상 인지시키기
# - 모델링 : CNN, colab
# - 모델링 방법
#     - 목적 : 특정 사진이 들어 갔을 때, 사람 얼굴을 인지하고, 그 부분의 색중 대부분의 색을 뽑아내어, 매치시키기
#         - Mean-shift clustering이라는 이미지 세그먼테이션 기법 ( 대표색 뽑아내기 )( 이게 구현이 쉬워 ) ( 정 안될 때, 최후의 보루)
#         - Foreground Extraction 기법 사용( 주요 오프젝트 추출하기 )
#           ( GrabCut 알고리즘( 대상 물체 라인따는 알고리즘 )을 활용하여 Foreground Extraction을 수행 )
#         - 위의 두가지 알고리즘을 대표하는 딥러닝 기법 ( GRAD-CAM )
#         - Grad-CAM heatmap 정보와 guided backpropagation 정보를 혼합해서 GrabCut 알고리즘의 초기 mask로 사용하면 위에서 나열했던 여러 가지 문제점을 해결할 수 있음. 최종적으로 추출해낸 foreground 영역과 색상 정보
#         
#     - 사람 피부색에 해당하는 컬러셋 확보
#         - 선행되야할 고민
#         
#             - 무슨 모델로 학습시킬 것인가?
#             - 연속적인 데이터 처리는 어떻게 해야할까?
#         
#     - 이미지 인지는, CNN 을 통해 하고 GRID-CAM을 적용하는 것

# #### https://github.com/sjchoi86/deep-uncertainty/blob/master/code/demo_gradcam_resnet50.ipynb

• 위의 이미지에서 시각화에 준 condition(Cat / Dog)에 따라 그에
대응되는 부분만 표시해주는 것을 볼 수 있음
• 이미지에서 heatmap을 계산하는 것이므로 앞에서 나온 Guided
Backpropagation과 결합해 Guided-Grad-CAM으로도 사용 가능

    class GradCAM:

  def __init__(self, module, target_layer):
    self.module = module
    self.target_layer = target_layer
    self.target_output = None
    self.target_output_grad = None

    def forward_hook(_, __, output):
      self.target_output = output.clone()
    
    def backward_hook(_, __, grad_output):
      assert len(grad_output) == 1
      self.target_output_grad = grad_output[0].clone()

    self.target_layer.register_forward_hook(forward_hook)
    self.target_layer.register_backward_hook(backward_hook)

    def forward_pass(self, image):
      self.module.eval()
      self.module.zero_grad()
      return self.module(image)

    def get_grad_cam(self, image, target_class = None):
      assert len(image.size()) == 3
      image = image.unsqueeze(0)
      out = self.forward_pass(image)
      if target_class is None:
        target_class = torch.argmax(out).item()
        print('Target class is {}({})'.format(target_class, utils.index_to_class(target_class)))

      onehot = utils.onehot(target_class, out_size(1))
      onehot = onehot.unsqueeze(0)
      out.backward(onehot)

      grad = self.target_output_grad
      grad = F.adaptive_avg_pool2d(grad, 1)

      feature = self.target_output
      feature = feature*grad
      feature = torch.sum(feature, dim =1)
      feature = F.relu(feature)

      return feature.squeeze()

# #### skin_Detection 방법 1
#
# - opencv 방법
#     - 목적이 skin_Detection 을 한 후에

# +
import cv2
import numpy as np

#Open a simple image
img=cv2.imread("6_A_hgr2B_id05_1.jpg")

#converting from gbr to hsv color space
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#skin color range for hsv color space 
HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

#converting from gbr to YCbCr color space
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#skin color range for hsv color space 
YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

#merge skin detection (YCbCr and hsv)
global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
global_mask=cv2.medianBlur(global_mask,3)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))


HSV_result = cv2.bitwise_not(HSV_mask)
YCrCb_result = cv2.bitwise_not(YCrCb_mask)
global_result=cv2.bitwise_not(global_mask)


#show results
# cv2.imshow("1_HSV.jpg",HSV_result)
# cv2.imshow("2_YCbCr.jpg",YCrCb_result)
# cv2.imshow("3_global_result.jpg",global_result)
# cv2.imshow("Image.jpg",img)
cv2.imwrite("1_HSV.jpg",HSV_result)
cv2.imwrite("2_YCbCr.jpg",YCrCb_result)
cv2.imwrite("3_global_result.jpg",global_result)
cv2.waitKey(0)
cv2.destroyAllWindows()  
# -







