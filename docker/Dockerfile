FROM ros:jazzy-ros-base
WORKDIR /root/ros2_ws
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y ros-jazzy-cv-bridge
RUN pip install torch==2.6.0 torchvision==0.21.0 xformers --index-url https://download.pytorch.org/whl/cu124 --break-system-packages
RUN pip install timm --break-system-packages
RUN pip install einops --break-system-packages
RUN pip install omegaconf --break-system-packages
RUN pip install scipy --break-system-packages
RUN pip install numpy --break-system-packages
RUN pip install scikit-image --break-system-packages
RUN pip install imageio --break-system-packages
RUN pip install pyyaml --break-system-packages
RUN pip install open3d --break-system-packages
ENV PYTHONPATH $PYTHONPATH:/root/Fast-FoundationStereo
RUN git -C /root clone https://github.com/NVlabs/Fast-FoundationStereo.git
COPY /20-30-48 /root/Fast-FoundationStereo/weights/20-30-48
RUN mkdir -p src
RUN git -C src/ clone https://github.com/jfrancis71/ros2_fast_foundationstereo.git
RUN colcon build --symlink-install
CMD /bin/bash -c "source ./install/setup.bash; ros2 run ffs ffs_node"
