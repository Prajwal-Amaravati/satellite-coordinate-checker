import concurrent.futures


def multiprocess_func(worker_func, entity):
    try:
        num_processes = min(len(entity), 8)
        chunk_size = len(entity) // num_processes
        input_chunks = [
            entity[i : i + chunk_size] for i in range(0, len(entity), chunk_size)
        ]
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=num_processes
        ) as executor:
            results = list(executor.map(worker_func, input_chunks))
        return results
    except:
        raise Exception("Error in multiprocessing chunks, func")
