import os
import threading
import time
from multiprocessing import Process
from pathlib import Path

import requests


def encrypt_file(path: Path):
    print(f"Processing file from {path} in process {os.getpid()}")
    _ = [i for i in range(100_000_000)]


def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    start = time.perf_counter()

    file_path = Path("rockyou.txt")
    image_url = "https://picsum.photos/1000/1000"

    # Multithreading for downloading image
    image_thread = threading.Thread(target=download_image, args=(image_url,))
    image_thread.start()

    # Multiprocessing for file encryption
    encrypt_process = Process(target=encrypt_file, args=(file_path,))
    encrypt_process.start()

    image_thread.join()
    encrypt_process.join()

    finish = time.perf_counter()
    print(f"Time taken: {finish - start} seconds")
