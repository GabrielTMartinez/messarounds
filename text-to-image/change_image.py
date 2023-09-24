"""
Copyright 2023 Timothy Brooks, Aleksander Holynski, Alexei A. Efros

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Portions of code and models (such as pretrained checkpoints, which are fine-tuned starting from released Stable Diffusion checkpoints) are derived from the Stable Diffusion codebase (https://github.com/CompVis/stable-diffusion). Further restrictions may apply. Please consult the Stable Diffusion license `stable_diffusion/LICENSE`. Modified code is denoted as such in comments at the start of each file. 
"""
import sys

import torch
from PIL import Image, ImageOps
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler

if len(sys.argv) <= 2:
    raise Exception("You need to pass the image name and the prompt!")

image_name = sys.argv[1]
prompt = sys.argv[2]

model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
pipe.to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)


def get_image(image_path):
    local_image = Image.open(f'images/{image_path}')
    local_image = ImageOps.exif_transpose(local_image)
    local_image = local_image.convert("RGB")
    return local_image


image = get_image(image_name)

images = pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images
images[0].save(f"images/{image_name}_changed.png")
