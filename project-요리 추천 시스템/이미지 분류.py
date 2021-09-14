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

# + id="9dxp6vi5E-Mc"
https://github.com/junkwhinger/grad_cam
여기서 보고 하자 금방하겠다
https://github.com/insikk/Grad-CAM-tensorflow/blob/master/gradCAM_tensorflow_VGG16_demo.ipynb

# + id="yP4M3nTMGYkb" executionInfo={"status": "ok", "timestamp": 1631587048457, "user_tz": -540, "elapsed": 89018, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
import os
import zipfile
local_zip = '/content/drive/MyDrive/archive.zip'

zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()
#기본경로
base_dir = '/content/'

# + id="yFwh4TekLS7v" executionInfo={"status": "ok", "timestamp": 1631587443185, "user_tz": -540, "elapsed": 247, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
from pathlib import Path
import os.path
import matplotlib.pyplot as plt
import tensorflow as tf

# + id="Wz_Sdh7NQoTZ" executionInfo={"status": "ok", "timestamp": 1631587549426, "user_tz": -540, "elapsed": 225, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
import pandas as pd

# + id="bZOF-5hRMgcn" executionInfo={"status": "ok", "timestamp": 1631589700547, "user_tz": -540, "elapsed": 272, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
import numpy as np

# + [markdown] id="wTFrqd7sFDGV"
# [링크 텍스트](https://)# 새 섹션

# + id="KgtDYEhdRAhw" executionInfo={"status": "ok", "timestamp": 1631587514561, "user_tz": -540, "elapsed": 528, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
# Create a list with the filepaths for training and testing
train_dir = Path('/content/train')
train_filepaths = list(train_dir.glob(r'**/*.jpg'))

test_dir = Path('/content/test')
test_filepaths = list(test_dir.glob(r'**/*.jpg'))

val_dir = Path('/content/validation')
val_filepaths = list(test_dir.glob(r'**/*.jpg'))


# + id="R91RESsNRA13" executionInfo={"status": "ok", "timestamp": 1631587525534, "user_tz": -540, "elapsed": 231, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
def proc_img(filepath):
    """ Create a DataFrame with the filepath and the labels of the pictures
    """

    labels = [str(filepath[i]).split("/")[-2] \
              for i in range(len(filepath))]

    filepath = pd.Series(filepath, name='Filepath').astype(str)
    labels = pd.Series(labels, name='Label')

    # Concatenate filepaths and labels
    df = pd.concat([filepath, labels], axis=1)

    # Shuffle the DataFrame and reset index
    df = df.sample(frac=1).reset_index(drop = True)
    
    return df



# + id="54A_2BCPRBAY" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1631587554073, "user_tz": -540, "elapsed": 243, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="d0dfa2be-2e5c-4b65-c5e0-6d2d8610d11e"
train_df = proc_img(train_filepaths)
test_df = proc_img(test_filepaths)
val_df = proc_img(val_filepaths)
print('-- Training set --\n')
print(f'Number of pictures: {train_df.shape[0]}\n')
print(f'Number of different labels: {len(train_df.Label.unique())}\n')
print(f'Labels: {train_df.Label.unique()}')

# + id="gMe5KF63RyC-" colab={"base_uri": "https://localhost:8080/", "height": 204} executionInfo={"status": "ok", "timestamp": 1631587562400, "user_tz": -540, "elapsed": 414, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="775dd5c7-85f0-42db-92c8-b863e8a05fa1"
# The DataFrame with the filepaths in one column and the labels in the other one
train_df.head(5)

# + id="xZqfk4vmR_fu" colab={"base_uri": "https://localhost:8080/", "height": 525} executionInfo={"status": "ok", "timestamp": 1631587571299, "user_tz": -540, "elapsed": 7612, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="b5e76b04-701e-441a-9ba1-5c82b0502c81"
# Create a DataFrame with one Label of each category
df_unique = train_df.copy().drop_duplicates(subset=["Label"]).reset_index()

# Display some pictures of the dataset
fig, axes = plt.subplots(nrows=6, ncols=6, figsize=(8, 7),
                        subplot_kw={'xticks': [], 'yticks': []})

for i, ax in enumerate(axes.flat):
    ax.imshow(plt.imread(df_unique.Filepath[i]))
    ax.set_title(df_unique.Label[i], fontsize = 12)
plt.tight_layout(pad=0.5)
plt.show()


# + id="giQ3YoyQSCro" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1631587582516, "user_tz": -540, "elapsed": 932, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="89ea70eb-3131-4d49-db92-1b84de14f36e"
train_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input
)

test_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input
)

train_images = train_generator.flow_from_dataframe(
    dataframe=train_df,
    x_col='Filepath',
    y_col='Label',
    target_size=(224, 224),
    color_mode='rgb',
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=0,
    rotation_range=30,
    zoom_range=0.15,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    fill_mode="nearest"
)

val_images = train_generator.flow_from_dataframe(
    dataframe=val_df,
    x_col='Filepath',
    y_col='Label',
    target_size=(224, 224),
    color_mode='rgb',
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    seed=0,
    rotation_range=30,
    zoom_range=0.15,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    fill_mode="nearest"
)

test_images = test_generator.flow_from_dataframe(
    dataframe=test_df,
    x_col='Filepath',
    y_col='Label',
    target_size=(224, 224),
    color_mode='rgb',
    class_mode='categorical',
    batch_size=32,
    shuffle=False
)

# + id="OKgsrv-oSJJb" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1631587603256, "user_tz": -540, "elapsed": 7269, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="44f68d55-67f3-4f42-9b77-f16c8e7d4769"
# Load the pretained model
# mobileNetV2를 사용
# 정보 손실을 최소화하기 위함
pretrained_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet',
    pooling='avg'
)
pretrained_model.trainable = False

# + id="nO7aGBwnSMx4" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1631588393645, "user_tz": -540, "elapsed": 790398, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="f15d2c96-3d2d-4dda-dff3-dad3067fc531"
# 다중신경망 생성
# 128개의 신경망 구성
# 2개의층
#
inputs = pretrained_model.input

# mobileNet2로 한번 하고
# 다중 신경망 구성
# 다중 신경망 가기전에 마지막 레이어에서 grad cam으로 object detection 추가 예정

x = tf.keras.layers.Dense(128, activation='relu')(pretrained_model.output)
x = tf.keras.layers.Dense(128, activation='relu')(x)

# 36개의 재료임으로 36개 구성
outputs = tf.keras.layers.Dense(36, activation='softmax')(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)

# 옵티마이저 adma, loss는 categorical_crossentropy 사용
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_images,
    validation_data=val_images,
    batch_size = 32,
    epochs=5,
    # 과적합을 막기위해 Earylstoping 사용
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=2,
            restore_best_weights=True
        )
    ]
)

# + id="1zQpxBtDSW3Q"
# 검증 그래프 넣을부분


# + id="O0mzmIv0SW6G" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1631589727265, "user_tz": -540, "elapsed": 19671, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="761c40e9-004b-4118-9c3e-de7f8568cfa9"
# Predict the label of the test_images

# 테스트 셋을 활용한 예측
pred = model.predict(test_images)
# numpy로 변환
pred = np.argmax(pred,axis=1)

# Map the label
labels = (train_images.class_indices)
labels = dict((v,k) for k,v in labels.items())
pred = [labels[k] for k in pred]

y_test = [labels[k] for k in test_images.classes]

# + id="sL4UvX5_SW9E" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1631589734323, "user_tz": -540, "elapsed": 633, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="6c33d267-836f-46d0-c1e7-79d29a241ad7"
# 정확도 보기
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_test, pred)
print(f'Accuracy on the test set: {100*acc:.2f}%')

# + colab={"base_uri": "https://localhost:8080/", "height": 665} id="q_FzwS90VT9D" executionInfo={"status": "ok", "timestamp": 1631589745325, "user_tz": -540, "elapsed": 5847, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="85edaf61-2b83-4743-ca2b-2cb4f1f7af35"
#heat map 생성
# heat map에서 grad cam을 활용하고 여기서
# grap cut을 활용하여 object detection을 하기위함

from sklearn.metrics import confusion_matrix
import seaborn as sns

cf_matrix = confusion_matrix(y_test, pred, normalize='true')
plt.figure(figsize = (15,10))
sns.heatmap(cf_matrix, 
            annot=True, 
            xticklabels = sorted(set(y_test)), 
            yticklabels = sorted(set(y_test)),
            )
plt.title('Normalized Confusion Matrix')
plt.show()

# + id="ywR2LUGH4sWm" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1631589756333, "user_tz": -540, "elapsed": 5609, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="12fc282b-23f7-4935-d088-6e194f5608e2"
# Display some pictures of the dataset with their labels and the predictions
# 아이템 예측하기 및 정확도

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15),
                        subplot_kw={'xticks': [], 'yticks': []})

for i, ax in enumerate(axes.flat):
    ax.imshow(plt.imread(test_df.Filepath.iloc[i]))
    ax.set_title(f"True: {test_df.Label.iloc[i]}\nPredicted: {pred[i]}")
plt.tight_layout()
plt.show()

# + id="GO8tzBU74sZf" executionInfo={"status": "ok", "timestamp": 1631589769038, "user_tz": -540, "elapsed": 220, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}}
import matplotlib.cm as cm

def get_img_array(img_path, size):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=size)
    array = tf.keras.preprocessing.image.img_to_array(img)
    # We add a dimension to transform our array into a "batch"
    # of size "size"
    array = np.expand_dims(array, axis=0)
    return array

  
def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    # First, we create a model that maps the input image to the activations
    # of the last conv layer as well as the output predictions
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    # Then, we compute the gradient of the top predicted class for our input image
    # with respect to the activations of the last conv layer
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    # This is the gradient of the output neuron (top predicted or chosen)
    # with regard to the output feature map of the last conv layer
    grads = tape.gradient(class_channel, last_conv_layer_output)


    # This is a vector where each entry is the mean intensity of the gradient
    # over a specific feature map channel
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # We multiply each channel in the feature map array
    # by "how important this channel is" with regard to the top predicted class
    # then sum all the channels to obtain the heatmap class activation
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # For visualization purpose, we will also normalize the heatmap between 0 & 1
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

def save_and_display_gradcam(img_path, heatmap, cam_path="cam.jpg", alpha=0.4):
    # Load the original image
    img = tf.keras.preprocessing.image.load_img(img_path)
    img = tf.keras.preprocessing.image.img_to_array(img)

    # Rescale heatmap to a range 0-255
    heatmap = np.uint8(255 * heatmap)

    # Use jet colormap to colorize heatmap
    jet = cm.get_cmap("jet")

    # Use RGB values of the colormap
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]

    # Create an image with RGB colorized heatmap
    jet_heatmap = tf.keras.preprocessing.image.array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
    jet_heatmap = tf.keras.preprocessing.image.img_to_array(jet_heatmap)

    # Superimpose the heatmap on original image
    superimposed_img = jet_heatmap * alpha + img
    superimposed_img = tf.keras.preprocessing.image.array_to_img(superimposed_img)

    # Save the superimposed image
    superimposed_img.save(cam_path)

    # Display Grad CAM
#     display(Image(cam_path))
    
    return cam_path
    
preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions

last_conv_layer_name = "Conv_1"
img_size = (224,224)

# Remove last layer's softmax
model.layers[-1].ativation = None

# + id="nrxqJs7g4sdw" colab={"base_uri": "https://localhost:8080/", "height": 1000} executionInfo={"status": "ok", "timestamp": 1631589785755, "user_tz": -540, "elapsed": 11294, "user": {"displayName": "\ub450\ub4dc\ub9bc", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GjzXad5nuvxpsURPSSa0wwNUQw7ZxAVNBPF9kyp=s64", "userId": "16001116907625236704"}} outputId="cba82468-55bc-42b2-e9fa-1501cc4e0a66"
# Display the part of the pictures used by the neural network to classify the pictures
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15),
                        subplot_kw={'xticks': [], 'yticks': []})

for i, ax in enumerate(axes.flat):
    img_path = test_df.Filepath.iloc[i]
    img_array = preprocess_input(get_img_array(img_path, size=img_size))
    heatmap = make_gradcam_heatmap(img_array, model, last_conv_layer_name)
    cam_path = save_and_display_gradcam(img_path, heatmap)
    ax.imshow(plt.imread(cam_path))
    ax.set_title(f"True: {test_df.Label.iloc[i]}\nPredicted: {pred[i]}")
plt.tight_layout()
plt.show()

# + id="FQuf5CfS4shb"
# 이제 grab cam으로 감싼 부분 detection해보자잇
# 제일 큰 부분 감싸면 되것지

# + id="A4hHXGC44so2"


# + id="psXLuGz240HP"


# + id="Pvenw2zq40Jq"


# + id="7PMOxZPx40Nt"


# + id="ufS3Bpup40QI"


# + id="9GWk99zF40Tz"


# + id="Q0NJmFXh40WG"


# + id="k2Eat3av40Yp"


# + id="udu72eEjSXAS"
이거 바꿔보쟈잇!
