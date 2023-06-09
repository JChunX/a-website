## **ABOUT**

**Hi, I'm Jason 🤠**

I am a 2nd year Robotics grad student at the University of Pennsylvania with a knack for building software that interacts with our physical world.

- I am currently working on deep learning and computer vision for autonomous trucks at Kodiak Robotics.
- I am also part of the Lifelong Machine Learning Group at GRASP, where I build machine learning systems for household robots and embodied autonomy.
- Seeking full-time software engineering roles starting Spring 2024.

## **PROJECTS**

### **F1Tenth Autonomous Racing** - Spring 2023
<img src="static/images/drag_race.jpeg" alt="three f1tenth vehicles lined up side-by-side on the track" width="600"/>

**Technologies:** Python, C++, ROS2, PyTorch, TensorRT, Drake

Goal: Don't crash and minimize laptime.

How: Implement a robust, safe, and fast autonomy stack on the NVIDIA Jetson edge computer.

What we did:

- Perception: Convolutional LiDAR outlier rejection, Hardware-accelerated Bresenham collision detection, Obstacle tracking, Neural object detection with TensorRT
- Planning: Custom frenet frame planner, Direct collocation + mininum curvature trajectory optimization, RRT*
- Control: Hardware-accelerated LQR, Adaptive cruise control, Disparity-extended gap-following, Time-to-collision based obstacle avoidance
- Operations: Custom telemetry bringup and recording, Visualization on Foxglove Studio

What we achieved:

- **1st place**, Penn ESE 615 F1Tenth Race 2&3
- **1st place**, 12th F1Tenth Autonomous Grand Prix @ CPS-IoT 2023

### **Contrastive Reward Functions for Embodied Agents** - Spring 2023
<img src="static/images/650_final_proj.png" alt="contrastive reward model" width="600"/>

**Technologies:** Python, PyTorch, Ai2Thor, OpenAI CLIP

Leveraging the power of CLIP (Contrastive Language-Image Pre-training), we adapt CLIP embeddings to learn a dense reward function for embodied agents. Using a transformer-based architecture, the reward model learns to pair video frames and corresponding language instructions by minimizing the InfoNCE loss. We showcase the model's potential for fine-tuning sparse reward tasks by demonstrating its ability to return appropriate rewards in a variety of scenarios.

### **Neural-Inertial Odometry Sensor Fusion on the F1Tenth Platform** - Spring 2023
<img src="static/images/local_inn.gif" alt="visualization of local_inn sensor fusion" width="600"/>

**Technologies:** PyTorch, TensorRT, Python

Improved the robustness of a normalizing-flow based lidar localization system (Local_INN) by fusing IMU accelerometer data with neural network odometry estimates using an Unscented Kalman Filter. Created a ROS2 package for the system as a drop-in replacement for the particle filter-based localization system used by the F1Tenth platform.

### **Quadruped MPC Gait Transitions** - Fall 2022
<img src="static/images/mpc_gait_trans.png" alt="quadruped mpc gait transitions" width="600"/>
<img src="static/images/gait_trans_opt_fsm.png" alt="gait transitions finite state machine" width="600"/>

**Technologies:** Drake, Mujoco, Python, C++

We are interested in the problem of transitioning between two different gaits for a quadruped robot. Building upon an existing convex MPC method for gait planning, we extend it to handle gait transitions by planning over multiple potential next gait states.

### **Mini Minecraft** - Summer 2022
<img src="static/images/mini_mc.png" alt="panoramic view of mini minecraft game footage" width="600"/>

**Technologies:** C++, OpenGL

Adventures in 3D computer graphics and multi-threaded C++ programming. A simple Minecraft clone implementing custom shaders, voxel terrain generation, chunk management, and rendering.

### **Prosthetic Leg Software** - Spring 2022
<img src="static/images/pack.png" alt="expanded view of a prosthetic leg knee joint" width="600"/>

**Technologies:** C++, Python, Tensorflow, ROS2, OpenCV, PyBullet

I led the software development at NCSU Pack Bionics, a student organization that designs and builds prosthetic legs for the Cybathlon Competition. Starting from scratch, I helped create the software stack for our prosthetic leg, including a Pybullet-ROS2 bridge for simulation, a vision-based gait planner, and an imitation learning based gait controller.

## **EDUCATION**

### **University of Pennsylvania** (2022-2024)

MSE, Robotics

### **University of North Carolina at Chapel Hill** (2018-2022)

BS, Computer Science & Biomedical Engineering
