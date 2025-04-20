from PIL import Image, ImageFilter, ImageEnhance
import os, asyncio, time, json
from concurrent.futures import ThreadPoolExecutor
from chart import create_chart

async def get_files(dir):
    return await asyncio.to_thread(os.listdir, dir)

async def edit(image, exec):
        loop = asyncio.get_running_loop()
        def _edit():
            img = Image.open(f"./images/{image}")
            embossed = img.filter(ImageFilter.EMBOSS)
            enhanced = ImageEnhance.Contrast(embossed).enhance(3.0)
            enhanced.save(f"../data/images/embossed/{image}")
            blurred = img.filter(ImageFilter.GaussianBlur(6))
            blurred.save(f"../data/images/blurred/{image}")
        await loop.run_in_executor(exec, _edit)

async def edit_all(exec):
    files = await get_files("./images")
    tasks = []
    for file in files:
        tasks.append(edit(file, exec))
    await asyncio.gather(*tasks)

def main():
    max_workers = 8
    content = []
    print("IMAGE EDITING TIME")
    for workers in range(max_workers, 0, -1):
        start = time.time()
        executor = ThreadPoolExecutor(max_workers=workers)
        asyncio.run(edit_all(executor))
        t = round((time.time()-start), 4)
        print(f"Threads: {workers} Time: {t} seconds")
        content.append({"threads": workers, "seconds": t })
    with open("./times.json", "w") as f:
        json_data = json.dumps(content, indent=2)
        f.write(json_data)  

if __name__ == "__main__":
    main()
    create_chart()