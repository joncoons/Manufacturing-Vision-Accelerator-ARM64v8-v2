Through experimentations, trial and testing,  building the ONNX runtime wheel on the target device using Jetpack 4.6.1 or older yields the best performance observed.

Include in this repository is a Dockerfile_on_jetson.arm64v8 which provides the docker build you would run on your Nano, NX or Xavier device.  There are instructions for performing the build via the CLI of your device in the top comments section.

This container then becomes the main base container for the Dockerfile.arm64v8

For convenience, I've alson posted a build of this to my open container repository at:

visionaccelerator.azurecr.io/edge_base/arm64v8/onnxruntime_jp451:1.6.0-arm64v8 

This is also included in the Dockerfile.arm64v8 file.  The build includes both torch and torchvision as well.