import cv2
import os
import streamlit as st


def record_dataset(banner_id, name):
    st.write("Recording dataset...")
    # Create folder to store images if it doesn't exist
    folder_name = f"{banner_id}_{name}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Open camera
    cap = cv2.VideoCapture(0)

    # Continuously display live feed and record images
    for i in range(200):
        ret, frame = cap.read()
        if ret:
            # Display live feed
            st.image(frame, channels="BGR")

            # Save image to folder
            image_path = os.path.join(folder_name, f"{i}.jpg")
            cv2.imwrite(image_path, frame)

    cap.release()
    st.write("Dataset recorded successfully!")


def main():
    st.title("Dataset Recorder")
    st.write("Enter your Banner ID and Name:")
    banner_id = st.text_input("Banner ID")
    name = st.text_input("Name")

    if st.button("Record Dataset"):
        if banner_id and name:
            record_dataset(banner_id, name)
        else:
            st.write("Please enter your Banner ID and Name.")

    if st.button("Retake Dataset"):
        st.write("Retake Dataset button clicked!")
        # Add functionality to retake dataset here


if __name__ == "__main__":
    main()
