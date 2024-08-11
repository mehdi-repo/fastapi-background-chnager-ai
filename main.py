
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import aiohttp
import io
import os
from rembg import remove

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Set your OpenAI API key here
openai_api_key = 'sk-proj-4E3MLkNGlLnWmoMuJuLgeAeP8cQrp0 .....'

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...), prompt: str = Form(...)):
    if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    try:
        # Remove background
        input_image = Image.open(io.BytesIO(await file.read())).convert("RGBA")
        removed_bg_image = remove(input_image)
        
        # Generate new background
        new_background = await generate_background(prompt)
        
        # Combine images
        final_image = combine_images(removed_bg_image, new_background)
        
        # Save the final image
        final_image_path = "final_image.png"
        final_image.save(final_image_path)

        return {"filename": final_image_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image processing failed: {str(e)}")




@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(filename)
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=filename, media_type='image/png')
    raise HTTPException(status_code=404, detail="File not found")

async def generate_background(prompt: str):
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/images/generations", headers=headers, json=data) as response:
            response.raise_for_status()
            image_url = (await response.json())['data'][0]['url']
            async with session.get(image_url) as image_response:
                image = Image.open(io.BytesIO(await image_response.read()))
                return image

def combine_images(foreground_image, background_image):
    foreground_image = foreground_image.convert("RGBA")
    background_image = background_image.convert("RGBA")
    background_image = background_image.resize(foreground_image.size)
    combined_image = Image.alpha_composite(background_image, foreground_image)
    return combined_image.convert("RGB")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
