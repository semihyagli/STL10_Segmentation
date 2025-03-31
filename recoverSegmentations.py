import argparse
import stl10
from PIL import Image, ImageDraw
import json
from numpy import array, arange, save
from matplotlib.pyplot import subplots
from itertools import chain 
import os

ALL = "all"

DEFAULT_TEST_X_BIN_LOC = "./data/stl10_binary/test_X.bin"
DEFAULT_TEST_Y_BIN_LOC = "./data/stl10_binary/test_y.bin"

DEFAULT_SEGMENTED_TEST_X_SAVE_LOC = "./test_X_segmented.npy"

DEFAULT_NUM_SQUARES = 16
DEFAULT_TRANSPARENCY = 0.4
DEFAULT_DATA_LENGTH = 8000


LAYER_COLORS = {
  "0": "#ff8080",
  "1": "#ffd480",
  "2": "#d4ff80",
  "3": "#80ff80",
  "4": "#80ffd4",
  "5": "#80d4ff",
  "6": "#8080ff",
  "7": "#d580ff",
  "8": "#ff80d4",
}

LABEL_DICTIONARY = {
  1: "airplane",
  2: "bird",
  3: "car",
  4: "cat",
  5: "deer",
  6: "dog",
  7: "horse",
  8: "monkey",
  9: "ship",
  10: "truck",
}


def combine_lists(list_of_lists):
    flattened_list = chain.from_iterable(list_of_lists)
    return list(
        list(tuple_item) for tuple_item in set(
            tuple(list_item) for list_item in flattened_list
        )
    )
    
def cutout(
        img_index,
        combine_segments=True,
        create_cutout=True,
        show_segmented_image=False,
        save=False,
        to_array=False,
        img_bin_loc=DEFAULT_TEST_X_BIN_LOC,
        lbl_bin_loc=DEFAULT_TEST_Y_BIN_LOC,
        ):
    
    label = stl10.read_labels(lbl_bin_loc)[int(img_index)]
    segment = LABEL_DICTIONARY[label]
    segment_marks_json_loc = f"./stl10_test_{segment}.json"
    
    with open(segment_marks_json_loc, 'r') as f:
        segment_marks = json.load(f)

    marked_squares = segment_marks[str(img_index)]
    combined_marked_squares =  {f"{segment}_combined": combine_lists(marked_squares.values())}
    marked_squares_dictionary = combined_marked_squares if combine_segments else marked_squares

    all_images = stl10.read_all_images(img_bin_loc)
    img = Image.fromarray(all_images[int(img_index)]).convert("RGBA")

    directory_OriginalImage = f"./{segment}/original/"
    directory_SegmentedImage = f"./{segment}/cutout/"

    if save: 
        if not os.path.exists(directory_OriginalImage):
            os.makedirs(directory_OriginalImage, exist_ok=True)
        img.save(os.path.join(directory_OriginalImage, f"{img_index}.png"))
    imgWidth, imgHeight = img.size

    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    squareSize = min(imgWidth, imgHeight)/DEFAULT_NUM_SQUARES

    for lbl, segmentation in marked_squares_dictionary.items():
        overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        for y in arange(0, imgHeight, squareSize):
            for x in arange(0, imgWidth, squareSize):
                top_left = (x, y)
                bottom_right = (x + squareSize, y + squareSize)

                if [int(x / squareSize), int(y / squareSize)] not in segmentation:
                    if create_cutout:
                        draw.rectangle([top_left, bottom_right], fill="#000000")
                else:
                    if not create_cutout:
                        draw.rectangle([top_left, bottom_right], 
                                    fill=LAYER_COLORS.get(lbl[-1], "#ff8080") + format(int(DEFAULT_TRANSPARENCY * 255), '02X'),
                                    )

        segmented_image = Image.alpha_composite(img, overlay)
        if show_segmented_image:
            fig, ax = subplots()
            ax.imshow(segmented_image)
        if save:
            if not os.path.exists(directory_SegmentedImage):
                os.makedirs(directory_SegmentedImage, exist_ok=True)
            segmented_image.save(os.path.join(directory_SegmentedImage, f"{img_index}_{lbl}.png"))

        if to_array:
            return array(segmented_image.convert("RGB"))
        
def get_segmented_images_array():
    
    combined_segments = []
    for i in range(DEFAULT_DATA_LENGTH):
        print(f"Segmentation Progress: {100*(i+1)/DEFAULT_DATA_LENGTH:0f}%", end="\r")
        combined_segments.append(
            cutout(
              img_index=i,
              combine_segments=True,
              create_cutout=True,
              show_segmented_image=False,
              save=False,
              to_array=True,
              )
        )

    output = array(combined_segments)

    return output
        
        


if __name__ == "__main__":
    
    ## Note: Although I created many arguments for future use, midway through writing the script, I realized that use cases maybe vastly different for those who may use this dataset. 
    ## If the dataset turns out to be popular, I may revisit this file and continue working on this, otherwise I fear that this file will remain in this state forever...

    parser = argparse.ArgumentParser()

    parser.add_argument("--img_bin_loc", type=str, default=DEFAULT_TEST_X_BIN_LOC, help="Location of the original stl10 images.")
    
    parser.add_argument("--lbl_bin_loc", type=str, default=DEFAULT_TEST_Y_BIN_LOC, help="Location of the original stl10 image labels.")

    parser.add_argument("--combine_segments", type=bool, default=True, help="Whether to combine segments within a single image.")

    parser.add_argument("--create_cutout", type=bool, default=True, help="Whether to create cutout from segments. If this is set to false, segments will be overlayed with transparent colors.")

    parser.add_argument("--show_segmented_image", type=bool, default=False, help="Whether to show segmented image.")

    parser.add_argument("--save", type=bool, default=True, help="Whether to save original and segmented under {segment}/original and {segment}/cutout directories, respectively.")

    parser.add_argument("--to_array", type=bool, default=True, help="Whether to combine segments within a single image.")

    parser.add_argument("--img_index", type=str, default=ALL, help="Select image index.")

    parser.add_argument("--save_segmented_img_arr", type=bool, default=True, help="Whether to save the segmented images array.")

    parser.add_argument("--save_segmented_img_loc", type=str, default=DEFAULT_SEGMENTED_TEST_X_SAVE_LOC, help="Where to save the segmented images array.")

    args = parser.parse_args()

    if args.img_index == ALL:
        segmented_images_array = get_segmented_images_array()
        if args.save_segmented_img_arr:
            save(args.save_segmented_img_loc, segmented_images_array)
            

    
