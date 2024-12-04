# Image Capture with OpenCV

This project allows capturing images from a connected camera using OpenCV, with the functionality to label the captured images to create a dataset. The images are saved in directories corresponding to different classes, and the text in the window informs the user about the program's status.

## Requirements

To run this project, make sure to have the following dependencies installed:

- Python 3.x
- OpenCV
- Pillow (PIL)
- dotenv (for loading environment variables)

### Installing dependencies

1. Clone the repository or download the project files.
2. Create a virtual environment using **pipenv**:

   ```bash
   pipenv install

3. Activate the virtual environment:

    ```bash
    pipenv shell
    
Once you have activated the environment select the interpreter with the name of the environment

4. If you don't have pipenv installed yet, you can install it with:

    ```bash
    pip install pipenv
    


## Usage

1. Initial Setup:
    - Ensure the camera is connected and accessible by OpenCV.
    - If you use a custom font (as in the example), place the font in the ./fonts/ directory and specify the path in the code.

2. Running the script: To start capturing images from the camera, run the Python script:

    ```bash
    python collect_img.py

3. User Interactions:
    - The text in the camera window instructs you to press "Q" to start capturing images.
    - Once "Q" is pressed, the images will begin to be saved in directories organized by classes (e.g., ./data/0, ./data/1, etc.).
    -If the camera window is closed, the program will also stop automatically.
    
    
### Project Structure

```
image-capture-opencv/
│
├── collect_img.py           # Main script for image capture
├── .env                     # File to load environment variables
├── fonts/                   # Folder containing the custom font (if used)
│   └── Roboto-Regular.ttf   # Custom font
├── data/                    # Folder where captured images are saved
│   ├── 0/                   # Subdirectory for class 0
│   ├── 1/                   # Subdirectory for class 1
│   └── 2/                   # Subdirectory for class 2
└── README.md                # This file
```

### Code Explanation

1. Libraries Used:
    - OpenCV (cv2): Used to capture video from the camera, process images, and display the feed in real-time.
    - Pillow (PIL): Used for working with custom fonts and adding text over images.
    - dotenv: Used to load environment variables from a .env file to configure parameters like file paths or custom settings.

2. Program Flow:
    - Loading Environment Variables:
        - The .env file is used to load settings that may change (e.g., the font name or specific directories).
    - Image Capture:
        - The script starts by capturing images from the camera.
        - The text "Get ready! Press 'Q' to start capturing images" appears over the image to inform the user that the program is ready.
        - Once the user presses 'Q', the program starts capturing and storing the images in subdirectories within the data folder.
        
3. Saving Images:
    - The images are saved in the ./data/ directory within subdirectories corresponding to the current class (e.g., ./data/0, ./data/1).
    - The images are saved in .jpg format.
    
1. Propose new features: If you have any suggestions or new functionality you’d like to add, open an issue or create a pull request.
2. Fix bugs: If you find any bugs, please create an issue and/or submit a pull request with the fix.


        
