from memory_profiler import profile

@profile
def read_random():
    with open("./src/tests/lorem_ipsum.txt", "rb") as source:
        content = source.read(1024 * 10000)
        content_to_write = content[:]
    print("Content length: %d, content to write length %d" %
          (len(content), len(content_to_write)))
    with open("./src/tests/lorem_ipsum_out.txt", "wb") as target:
        target.write(content_to_write)

if __name__ == '__main__':
    read_random()