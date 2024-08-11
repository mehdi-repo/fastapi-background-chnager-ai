![My project-4](https://github.com/user-attachments/assets/96b522ee-4fbc-4d0d-9fed-2b49c2b5bd47)

# Image Background Changer with FastAPI

This project is a web application that allows users to upload an image, specify a background description, and process the image by removing its background and applying a new one based on the user's input. The processed image is then made available for download.

## Features

- **Image Upload**: Upload an image file through the web interface.
- **Background Description**: Provide a textual description of the desired background.
- **Background Removal**: Automatically remove the background from the uploaded image.
- **Background Replacement**: Generate a new background based on the description and combine it with the original image.
- **Download Processed Image**: Download the final processed image with the new background.
- **Responsive Design**: The website is fully responsive, ensuring a seamless experience across all devices.

## Technology Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend**: HTML, CSS (Bootstrap), Jinja2 Templates
- **Image Processing**: [Pillow (PIL)](https://pillow.readthedocs.io/), [aiohttp](https://docs.aiohttp.org/en/stable/)
- **Asynchronous Requests**: aiohttp for handling external API calls

## Installation

1. **Clone the repository:**



2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r req.txt
    ```

4. **Run the application:**

    ```bash
    python main.py
    uvicorn main:app --reload
    ```

5. **Access the web application:**

    Open your web browser and go to `http://127.0.0.1:8080`.

## Usage

1. **Upload an Image:** Click on the "Choose File" button to upload an image from your computer.
2. **Enter Background Description:** Provide a description of the desired background in the text field.
3. **Process the Image:** Click on "Upload and Process" to start the processing.
4. **Download the Image:** Once processing is complete, a download link will appear. Click it to download the processed image.

