import sys
from PIL import Image

def main():
    if len(sys.argv) != 2:
        print("שימוש: python show_channels.py <image_file>")
        return

    image_path = sys.argv[1]

    img = Image.open(image_path).convert("RGB")

    r, g, b = img.split()

    r.show(title="Red Channel")
    g.show(title="Green Channel")
    b.show(title="Blue Channel")

if __name__ == "__main__":
    main()
