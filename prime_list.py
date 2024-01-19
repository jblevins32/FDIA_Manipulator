

def get_prime_list(bit_length):

    file_path = r'C:\Users\jblevins32\PycharmProjects\malleability\primes.txt'  # Replace with your file path
    with open(file_path, 'r') as file:
        for line in file:
            if f"{bit_length}," in line:
                break

    prime = int(line.split(',')[1])
    return prime