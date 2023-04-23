import subprocess
subprocess.run(["python", "detect.py", "--source", "0", "--weights", "yolov5s.pt", "--view-img"])