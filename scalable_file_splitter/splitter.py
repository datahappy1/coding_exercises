import os

LARGE_FILE_PATH = "/home/pavel.prudky/Downloads/Python-3.9.0.tgz"
TARGET_FILES_TEMP_FOLDER = "/tmp/"
CHUNK_BYTE_SIZE = 5000000


def source_file_chunk_generator(filepath: str):
    processed_byte_size = 0
    file_byte_size = os.path.getsize(filepath)
    i = 0

    with open(filepath, mode="rb") as sf:
        while processed_byte_size <= file_byte_size:
            processed_byte_size += CHUNK_BYTE_SIZE
            i += 1
            yield i, sf.readlines(CHUNK_BYTE_SIZE)


def target_file_chunk_writer(chunk_id: int, chunk):
    with open(TARGET_FILES_TEMP_FOLDER + "chunk" + str(chunk_id), mode="ba") as tf:
        tf.writelines(chunk)


def main():
    for chunk_id, chunk in source_file_chunk_generator(filepath=LARGE_FILE_PATH):
        target_file_chunk_writer(chunk_id=chunk_id, chunk=chunk)


if __name__ == "__main__":
    main()
