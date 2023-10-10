from tkinter import *
from tkinter import ttk

import cv2
import cv2 as cv2
import numpy
from PIL import Image
from PIL import ImageTk
import os


class Program:
    def __init__(self, window):


        # self.output_dir = "output_images"  # Specify the directory where you want to save images
        # if not os.path.exists(self.output_dir):
        #     os.makedirs(self.output_dir)
        self.last_captured_frame = numpy.array([])

        self.window = window
        self.window.title("BRAIN TUMOR SEGMENTATION GUI")
        self.window.geometry("800x500")
        self.window.config(bg="#FFFFFF")

        self.notebook = ttk.Notebook()

        self.upload_tab = Frame(self.notebook)
        self.scan_tab = Frame(self.notebook)

        self.notebook.add(self.upload_tab, text="UPLOAD")
        self.notebook.add(self.scan_tab, text="SCAN")
        self.notebook.pack(expand=True, fill="both")

        # UPLOAD TAB
        self.upload_button = Button(self.upload_tab, text="UPLOAD IMAGE")
        self.image_label = Label(self.upload_tab, text="UPLOAD ANY IMAGE", width=80, height=20, bg='gray')
        self.prediction_box = Label(self.upload_tab, text="PRED_LABEL")
        self.upload_button.pack()
        self.image_label.pack()
        self.prediction_box.pack()

        # SCAN TAB
        self.title_label = Label(self.scan_tab, text= "SCAN MRI / X-RAY IMAGE", font=("Helvetica", 22))
        self.scan_image_label = LabelFrame(self.scan_tab, width=320, bg='white')
        self.image_scan = Label(self.scan_image_label, width=320, bg='white')
        self.title_label.pack()
        self.scan_image_label.pack(side='left', padx=20, pady=5)
        self.image_scan.pack(side='left', padx=20, pady=5)

        self.predict_button = Button(self.scan_tab ,text="CLICK IMAGE", width=30, height=3, font=("Helvetica", 12),
                                     command=self.click_image)
        self.predict_button.place(x=470, y = 150)
        self.retake_button = Button(self.scan_tab, text="RETAKE IMAGE", width=22, height=2, command=self.retake_image)
        self.predict_button = Button(self.scan_tab, text="PREDICT IMAGE", width=22, height=2, command=self.predict_image)
        self.retake_button.place(x=430, y=225)
        self.predict_button.place(x=620, y=225)

        # self.start_camera_button = Button(self.scan_tab, text="Start Camera", command=self.start_webcam_feed)
        # self.start_camera_button.pack()

        # Flag to track if the camera is started
        self.camera_started = False
        self.start_webcam_feed()

#    ###########################################################
#    #######--------START THE WEBCAM---------###################
#    ###########################################################
    def start_webcam_feed(self):
        # Check if the camera is already started
        if self.camera_started:
            return

        # Create a video capture object to access the webcam
        cap = cv2.VideoCapture(1)

        # Check if the camera is available
        if not cap.isOpened():
            self.image_scan.config(text="CONNECT CAMERA", font=("Helvetica", 16), padx=20, pady=20)
            return

        self.camera_started = True
        # self.start_camera_button.config(state="disabled")  # Disable the button while camera is active
        while self.camera_started:  # Continuously update the label with webcam frames
            ret, frame = cap.read()
            if ret:
                # Rotate the frame 90 degrees counter-clockwise
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                # Rotate the image by 180 degrees
                image = image.rotate(180)

                photo = ImageTk.PhotoImage(image=image)

                self.image_scan.config(image=photo, text="")  # Clear the text
                self.image_scan.image = photo
                self.window.update()  # Update the tkinter window

#    ###########################################################
#    #######--------CLICK THE IMAGE----------###################
#    ###########################################################
    def click_image(self):
        self.cap = cv2.VideoCapture(1)
        print("Check 1")
        if self.camera_started:
            print("Check 2")
            self.camera_started = False
        if self.cap is not None:
            print("Check 3")
            ret, frame = self.cap.read()
            if ret:
                print("Check 4")
                self.last_captured_frame = frame  # Store the frame in the variable
                # Reset the scan_image_label to display a message
                self.scan_image_label.config(text="Image captured", font=("Helvetica", 16), padx=20, pady=20)
            else:
                print("Failed to capture frame")
        cv2.destroyAllWindows()

        print("Last captured frame:", self.last_captured_frame)

        self.scan_image_label.config(text="CAMERA STOPPED", font=("Helvetica", 16), padx=20, pady=20)

    def retake_image(self):
        self.last_captured_frame = numpy.array([])
        self.start_webcam_feed()
        
    def predict_image(self):
        print("PREDICTING")

def main():
    window = Tk()
    app = Program(window)
    window.mainloop()


if __name__ == "__main__":
    main()



