import streamlit as st
import socket
import subprocess
import qrcode
import os

server_directory = os.getcwd()
print(server_directory)

# 创建目录用于存储上传文件
if not os.path.exists(server_directory+ "/upload"):
    os.makedirs(server_directory+ "/upload")

# 上传文件页面
colbutton1, colbutton2 = st.columns([8,2])
with colbutton1:
    st.write("## 上传文件")

# 文件上传
uploaded_file = st.file_uploader("选择要上传的文件", type=None)

if uploaded_file is not None:
    # 保存文件到服务器
    with open(os.path.join(server_directory+'/upload/', uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"文件 {uploaded_file.name} 上传成功！")

# 获取服务器的局域网 IPv4 地址
def get_local_ipv4():
    try:
        # 创建一个 UDP socket 并连接到外部服务器（例如 Google DNS 8.8.8.8）
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # 不需要实际发送数据
        ip = s.getsockname()[0]  # 获取本地IP地址
        s.close()
    except Exception as e:
        ip = "无法获取 IP 地址"
    return ip

# 显示局域网 IPv4 地址
local_ipv4 = get_local_ipv4()
st.write(f"访问如下地址上传文件： {local_ipv4}:9001")

ip=local_ipv4


# 生成二维码
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    return img

qr_img = generate_qr_code(f"http://{ip}:9001")
qr_img.save("upload/qr.png")

    # 将二维码显示在 Streamlit 上
st.image("upload/qr.png")

with colbutton2:
    st.write("")
    st.write("")
    st.markdown("[下载文件]("+f"http://{ip}:9000)")
    print(f"python -m http.server 9000 --directory \""+server_directory+"\"")
    subprocess.run(f"python -m http.server 9000 --directory \""+server_directory+"\"", shell=True)

