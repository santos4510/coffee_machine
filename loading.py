import time
def loading_animation(duration):
    animation = "|/-\\"
    idx = 0
    start_time = time.time()
    while time.time() - start_time < duration:
        print(f"\rLoading... {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)
    print("\rLoading... Done! ")