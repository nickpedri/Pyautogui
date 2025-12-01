import cv2 as cv
import os
import pyautogui as pag
import numpy as np
import functions as f


TEMPLATE_DIR = r"C:\Users\nickp\PythonWork\Pyautogui\scripts\number_extraction"


def load_templates():
    templates = {}
    for d in range(10):
        path = os.path.join(TEMPLATE_DIR, f"{d}.png")
        img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        templates[d] = img
    return templates


def preprocess(img, save_img=False):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, bw = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)

    if save_img:
        save_path = os.path.join(TEMPLATE_DIR, "processed_img.png")
        cv.imwrite(save_path, bw)

    return bw


def split_connected_digits(search_img):

    h, w = search_img.shape
    column_color = []
    for col in range(0, w):
        has_nonwhite = np.any(search_img[:, col] != 255)
        if has_nonwhite:
            column_color.append('black')
        else:
            column_color.append('white')

    digits = []
    in_digit = False
    start = 0
    for x, status in enumerate(column_color):
        if status == 'black' and not in_digit:
            # Starting a new digit
            in_digit = True
            start = x
        elif status == 'white' and in_digit:
            # Digit ends
            digit = search_img[:, start:x]
            digits.append(digit)
            in_digit = False
    # Close last digit if needed
    if in_digit:
        digits.append(search_img[:, start:w])

    # 3. Save each digit (for debugging)
    # for i, d in enumerate(digits):
        # save_path = os.path.join(TEMPLATE_DIR, f"digit_test_{i}.png")
        # cv.imwrite(save_path, d)
        # print(f"Saved digit {i} → {save_path}")

    return digits


def match_single_digit(img, templates):
    """
    Compare a digit image (img) with each template.
    Returns the recognized digit (0–9), or None if no match.
    """

    for digit, tmpl in templates.items():

        # Must match shape exactly
        if img.shape != tmpl.shape:
            continue

        # Exact pixel match
        if np.array_equal(img, tmpl):
            return digit

    return None


def decypher_digits(img_list, templates):
    """
    img_list: list of digit images returned from split_connected_digits()
    templates: dictionary mapping numbers 0–9 to template images
    Returns: the recognized number as an integer
    """
    result_str = ""

    for img in img_list:
        digit = match_single_digit(img, templates)

        if digit is None:
            raise ValueError(f"Unrecognized digit with shape {img.shape}")

        result_str += str(digit)

    return int(result_str)


def read_digits(img):
    # Load templates
    templates = load_templates()
    # print("Templates loaded:") if templates else print("Templates not loaded:")

    # Process screenshot
    processed = preprocess(img, save_img=True)
    digits = split_connected_digits(processed)
    digits = decypher_digits(digits, templates)
    print(digits)

