import os

if __name__ == '__main__':
    try:
        #print(os.environ)
        #os.environ["APIXU_KEY"]
        print("APIXU_KEY=" + os.environ["APIXU_KEY"])
    except KeyError:
        print("Please set the environment variable APIXU_KEY")
        sys.exit(1)
