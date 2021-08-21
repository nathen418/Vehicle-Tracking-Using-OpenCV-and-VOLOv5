[![Discord](https://discordapp.com/api/guilds/649703068799336454/widget.png)](https://discordapp.com/invite/KKYw763)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Antares-Network/Vehicle-Tracking-Using-OpenCV-and-VOLOv5?style=social)
![](https://img.shields.io/github/repo-size/Antares-Network/Vehicle-Tracking-Using-OpenCV-and-VOLOv5?color=Green&style=flat-square)
![](https://img.shields.io/tokei/lines/github/Antares-Network/Vehicle-Tracking-Using-OpenCV-and-VOLOv5?style=flat-square)  
![](https://cdn.discordapp.com/icons/649703068799336454/1a7ef8f706cd60d62547d2c7dc08d6f0.png) 

# Vehicle Tracking Using OpenCV and VOLOv5 (VTUOV)
- Description: This project is a vehicle tracking system using OpenCV and VOLOv5 designed to work with video streams or pre saved videos.

## Rough outline:
- This program is designed to detect a vehicle in a video stream and track it using OpenCV by subtracting the background and assigning groups of pixels to an object then given a unique ID. The coordinates are used to take a picture of the object and ask the YOLOv5 model to predict the object's class. If it is a vehicle the object is then tracked across the frame. If the vehicle moves enough the objects speed and direction is calculated and displayed on the frame as well as saved to a file. Direction is calculated using the length of  a straight line from the objects center point at the beginning of detection, to the center point at the end of detection divided by the number of pixels per meter. Speed is calculated using the distance between the two points in space.

# Early Beta footage:
![](/media/Early-beta-at-night.gif)
- Note: No YOLO detection is currently in use.

## How to run yourself:
- Clone the repository: `git clone https://github.com/Antares-Network/Vehicle-Tracking-Using-OpenCV-and-VOLOv5`
- Install the dependencies: `pip install -r requirements.txt`
- Run the program: `python main.py`
- Profit!


## End goal of the project:
- To be a drop in solution to detect and track the passage of vehicles on a highway or other road with accuracy such that the operator can get useful data about traffic flow for use in other applications. 

# objects.csv formatting
- Object ID, X position, Y position, Unix timestamp


## Credits:
- Nate Goldsborough: [Personal Website](https://nathen418.com)
- Garg Kunal : [Inspiration Repository](https://github.com/garg-kunal/object_tracker)

## Join our discord server:
https://dsc.gg/antaresnetwork

## License
- Yet to be Licensed
