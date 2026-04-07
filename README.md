# ros2_fast_foundationstereo

ROS2 bridge to integrate a ROS2 stereo camera with NVIDIA Fast-FoundationStereo model

## Summary

This docker image performs stereo depth prediction and can compute a disparity map and a point cloud and make this information available to the ROS2 system. It is similar to the stereo-image-proc node in ROS2. However it uses the NVIDIA Fast-FoundationStereo model (a PyTorch neural network) to make better predictions, particularly in low texture regions of the image. This docker image requires an NVIDIA GPU to run.

### Tested Hardware

Dell Precision Tower 2210, NVIDIA RTX2070

### Tested Software

Ubuntu 22.04, Docker version 28.2.2, CUDA 12.2


## Build and Deploy

To install:
```
git clone https://github.com/jfrancis71/ros2_fast_foundationstereo.git
cd ros2_fast_foundationstereo
```

In your browser go to: https://github.com/NVlabs/Fast-FoundationStereo
Locate the "Weights and Trade-off" section and follow instructions to download the checkpoint "20-30-48". You may need to unzip it and copy the weights into ./ros2_fast_foundationstereo/weights

Your folder should contain:

```
ros2_fast_foundationstereo/weights/20-30-48/cfg.yaml
ros2_fast_foundationstereo/weights/20-30-48/model_best_bp2_serialize.pth
```

To build docker image:
```
docker build -t ros2_ffs -f ./docker/Dockerfile ./weights/
```

To run:
```
docker run -it --rm --gpus=all --network=host --ipc=host ros2_ffs
```

### Subscribed Topics

- /left/image_rect_color
- /right/image_rect_color
- /left/camera_info
- /right/camera_info

### Published Topics

- /ffs_disparity
- /ffs_points2


## Licensing

Although this repository is licensed under an MIT Licence, it uses a number of components which are not. You should check suitability. In particular the NVIDIA Fast-Foundation Stereo has restrictions on commercial use. See https://github.com/NVlabs/Fast-FoundationStereo for licensing details.

## References

https://github.com/NVlabs/Fast-FoundationStereo

```
@article{wen2026fastfoundationstereo,
  title={{Fast-FoundationStereo}: Real-Time Zero-Shot Stereo Matching},
  author={Bowen Wen and Shaurya Dewan and Stan Birchfield},
  journal={CVPR},
  year={2026}
}
```
