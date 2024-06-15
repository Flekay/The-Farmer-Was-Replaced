def timer(callback):
    start = get_time()
    callback()
    quick_print(callback,"took:", str(get_time() - start), "seconds. Total time:", str(get_time() - runStart))