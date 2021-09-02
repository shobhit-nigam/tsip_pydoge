
#print("in one __name__ = ", __name__)

if __name__ == "__main__":
    def green():
        print("go green")
else:
    def green():
        print("bleed blue")


green()
