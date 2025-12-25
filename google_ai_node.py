import requests
import base64
from io import BytesIO
import torch
import numpy as np
from PIL import Image

class GoogleAIGenerateImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "api_key": ("STRING",),
                "model": ([
                "gemini-3-pro-image-preview"
            ],),
                "temperature": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.1}),
                "aspect_ratio": ([
                    "1:1",
                    "2:3",
                    "3:2",
                    "3:4",
                    "4:3",
                    "4:5",
                    "5:4",
                    "9:16",
                    "16:9",
                    "21:9"
                ], {"default": "9:16"}),
                "resolution": ([
                    "1k",
                    "2k",
                    "4k"
                ], {"default": "2k"}),
                "use_google_search": ("BOOLEAN", {"default": False})
            },
            "optional": {
                "proxy": ("STRING", {"default": ""}),
                "init_image1": ("IMAGE",),
                "init_image2": ("IMAGE",),
                "init_image3": ("IMAGE",),
                "init_image4": ("IMAGE",),
                "init_image5": ("IMAGE",),
                "init_image6": ("IMAGE",),
                "init_image7": ("IMAGE",),
                "init_image8": ("IMAGE",),
                "init_image9": ("IMAGE",),
                "init_image10": ("IMAGE",),
                "style": ("STRING", {"default": "", "multiline": True}),
                "num_images": ("INT", {"default": 1, "min": 1, "max": 4})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "generate"
    CATEGORY = "AI/Google"

    def generate(self, prompt, api_key, model, temperature=1.0, aspect_ratio="1:1", resolution="1k", use_google_search=False, proxy="", init_image1=None, init_image2=None, init_image3=None, init_image4=None, init_image5=None, init_image6=None, init_image7=None, init_image8=None, init_image9=None, init_image10=None, style="", num_images=1):
        import time
        start_time = time.time()
        
        # Validate API Key
        if not api_key or not api_key.strip():
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: API Key is empty!")
            raise ValueError("Please enter a valid Google AI API Key")
        
        # Setup proxy if provided
        proxies = None
        if proxy and proxy.strip():
            proxies = {
                "http": proxy.strip(),
                "https": proxy.strip()
            }
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Using proxy: {proxy.strip()}")
        else:
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] No proxy configured")
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] If connection fails, please configure a proxy (e.g., http://127.0.0.1:8800)")
        
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Starting image generation...")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Model: {model}")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Prompt: {prompt[:100]}..." if len(prompt) > 100 else f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Prompt: {prompt}")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Temperature: {temperature}")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Aspect Ratio: {aspect_ratio}")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Resolution: {resolution}")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Number of Images: {num_images}")
        
        # Convert images from ComfyUI tensor to base64 if provided
        image_data_list = []
        
        # Process all 10 possible input images
        init_images = [init_image1, init_image2, init_image3, init_image4, init_image5,
                      init_image6, init_image7, init_image8, init_image9, init_image10]
        
        num_input_images = sum(1 for img in init_images if img is not None)
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Found {num_input_images} input images to process...")
        
        for img_idx, init_image in enumerate(init_images):
            if init_image is not None:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Processing input image {img_idx + 1}/{num_input_images}...")
                # Take the first image from the batch
                image = init_image[0]
                # Convert from 0-1 range to 0-255 and to numpy array
                image = (image * 255).to(torch.uint8).numpy()
                # Create PIL image
                pil_image = Image.fromarray(image, mode="RGBA" if image.shape[2] == 4 else "RGB")
                # Convert to PNG bytes
                buffer = BytesIO()
                pil_image.save(buffer, format="PNG")
                # Convert to base64
                image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")
                image_data_list.append(image_data)
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Input image {img_idx + 1} processed successfully")

        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Preparing API request...")
        # Prepare API request
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        headers = {
            "Content-Type": "application/json"
        }

        # Build content parts
        parts = [{"text": prompt}]
        
        # Add all images to parts
        for i, image_data in enumerate(image_data_list):
            parts.append({
                "inlineData": {
                    "mimeType": "image/png",
                    "data": image_data
                }
            })
        
        # Add style if provided
        if style.strip():
            parts.append({"text": f"Style: {style}"})
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Added style prompt")

        # Add Google Search if enabled
        if use_google_search:
            parts.append({"text": "Use Google Search for reference"})
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Enabled Google Search")

        # Build generation config with imageConfig for aspect ratio and resolution
        generation_config = {
            "temperature": temperature,
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {
                "aspectRatio": aspect_ratio,
                "imageSize": resolution.upper()
            }
        }
        
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Using imageConfig: aspectRatio={aspect_ratio}, imageSize={resolution.upper()}")

        payload = {
            "contents": [{
                "parts": parts
            }],
            "generationConfig": generation_config,
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                }
            ]
        }

        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Sending request to Google AI API...")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Please wait, this may take a few seconds...")
        
        # Collect all generated images
        generated_images = []
        
        # Send multiple API requests to generate multiple images
        for i in range(num_images):
            if i > 0:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Generating image {i + 1}/{num_images}...")
            
            # Send API request
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=60, proxies=proxies)
                response.raise_for_status()  # Raise exception for non-200 status codes
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] API request {i + 1}/{num_images} completed successfully!")
            except requests.exceptions.Timeout:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: API request timed out after 60 seconds")
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Please check your network connection and proxy settings")
                raise
            except requests.exceptions.ConnectionError as e:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: Connection failed: {str(e)}")
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Please check your proxy settings (e.g., http://127.0.0.1:8800)")
                raise
            except requests.exceptions.RequestException as e:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: API request failed: {str(e)}")
                raise

            # Parse response
            result = response.json()
            if "candidates" not in result or not result["candidates"]:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: No candidates found in API response")
                raise ValueError("No candidates found in API response")

            # Get the first candidate (API returns 1 image per request)
            candidate = result["candidates"][0]
            
            if "content" not in candidate or "parts" not in candidate["content"]:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: No content found in candidate")
                raise ValueError("No content found in candidate")
            
            # Find the image data in the response
            generated_image_data = None
            for content_part in candidate["content"]["parts"]:
                if "inlineData" in content_part and "data" in content_part["inlineData"]:
                    generated_image_data = content_part["inlineData"]["data"]
                    break
            
            if not generated_image_data:
                print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] ERROR: No image data found in API response")
                raise ValueError("No image data found in API response")
            
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Decoding generated image {i + 1}/{num_images}...")
            # Convert base64 to PIL image
            generated_image_bytes = base64.b64decode(generated_image_data)
            generated_image = Image.open(BytesIO(generated_image_bytes))
            
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Converting image {i + 1}/{num_images} to ComfyUI format...")
            # Convert PIL image to numpy array
            generated_image = generated_image.convert("RGB")
            image_np = np.array(generated_image).astype(np.float32) / 255.0
            generated_images.append(image_np)
            
            print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Image {i + 1}/{num_images} processed successfully")
        
        end_time = time.time()
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Image generation completed successfully!")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Total time taken: {end_time - start_time:.2f} seconds")
        print(f"[Google AI Node] [{time.strftime('%H:%M:%S')}] Generated {len(generated_images)} image(s)")

        # Convert list of numpy arrays to a single tensor batch
        image_tensor = torch.from_numpy(np.stack(generated_images)).float()

        return (image_tensor,)
