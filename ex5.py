import zipfile
from tqdm import tqdm

# password list
dictionary = "english.txt"
# zip file to crack its password
zipFile = "locked.zip"

# initialize Zip File object
zipFile = zipfile.ZipFile(zipFile)
# count the number of passphrases
words = len(list(open(dictionary, "rb")))


with open(dictionary, "rb") as dictionary:
    for word in tqdm(dictionary, total=words, unit="word"):
        try:
            # extractall => exception whenever pwd incorrect
            #            => if correct - print pwd
            # strip => avoid newlines

            zipFile.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("\nPassword:", word.decode().strip())
            exit(0)
print("Password not found.")