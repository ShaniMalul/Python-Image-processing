import sys
import numpy as np
from PIL import Image

def stretch_histogram(gray_img):
    """
    מבצע מתיחת היסטוגרמה לתמונה בגווני אפור
    """
    arr = np.array(gray_img)

    min_val = arr.min()
    max_val = arr.max()

    # מניעת חלוקה באפס
    if max_val == min_val:
        return gray_img

    stretched = (arr - min_val) * 255 / (max_val - min_val)
    stretched = stretched.astype(np.uint8)

    return Image.fromarray(stretched)

def main():
    if len(sys.argv) != 2:
        print("Usage: python histogram_stretch.py <image_file>")
        return

    image_path = sys.argv[1]

    # א. קריאת קובץ תמונה
    img = Image.open(image_path)

    # ב. המרה לשחור / לבן
    gray = img.convert("L")

    # ג. חישוב היסטוגרמה
    histogram = gray.histogram()
    print("Histogram (first 20 values):")
    print(histogram[:20])

    # ד. מתיחת ההיסטוגרמה
    stretched_img = stretch_histogram(gray)

    # הצגת התמונות
    gray.show(title="Grayscale Image")
    stretched_img.show(title="Histogram Stretched Image")

    # שמירה לקובץ
    stretched_img.save("stretched_output.png")
    print("Saved stretched image as stretched_output.png")

if __name__ == "__main__":
    main()
