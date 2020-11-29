#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Yusuke Aita
# DATE CREATED: 20201128 (28th Nov. 2020)
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Retrieve the filenmaes from folder pet_images/
    filename_list = listdir("pet_images/")

    #Print 10 of the filenames from folder pet_images/
    for idx in ragne(0, 10, 1):
        print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]))

    results_dic = dict() # initialize the dictionary of pet labels

        # Determine number of items in Dictionary
    items_in_dic = len(results_dic) # should be 0
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    edited_filename_list = []

    for filename in filename_list:
        print("filename=", filename)

        # Create its petname from the filename
        pet_image = filename
        low_pet_image = pet_image.lower()
        word_list_pet_image = low_pet_image.split("_")
        print("type is", type(word_list_pet_image))

        # Create pet_name starting as empty string
        pet_name = ""
        print("type is", type(pet_name))

        # Loops to check if word in pet_name is only alphabetic characters
        # if true append word to pet_name separated by trailing space
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "

        # Strip off starting/trailing whitespace characters
        pet_name = pet_name.strip()


        #commandbox = filename.lower()
        #print("commandbox=", commandbox)
        edited_filename_list.append(pet_name)

        #results_dic[filename] = commandbox

    print("Edited_filename_list =", edited_filename_list)

    # results_dic = dict(zip(filename_list, edited_filename_list))

    print("\nDictionary is ", results_dic)

    # Adds new key-value pairs to dictionary ONLY shen key doesn't already exist. THis dictionary's value
    # is s List that contains only one item - the pet image label
    filenames = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
    pet_labels = ["beagle", "boston terrier"]
    for idx in range(0, len(filenames), 1):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("** Warning: Key=", filenames[idx],
                  "already exists in results_dic with value =",
                  results_dic[filenames[idx]])

    # Iterating through a dictionary priting all keys & their associated values
    print("\nPriting all key-value pairs in dictionary results_doc:")
    for key in results_dic:
        print("Filename=", key, "    Pet Label=", results_dic[key][0])

    # The best format for each pet image name would be:
    # Label: with only lower case letters
    # Blank space separating each word in a label composed of multiple words
    # Whitespace characters stripped from from & end of label

    # Sets pet_iamge variable to a filenmae
    pet_image = "Boston_terrier_02259.jpg"

    # Sets string to lower case letters
    low_pet_image = pet_image.lower()

    # Splits lower case string  by _ to breake into words
    wowrd_list_pet_image = low_pet_image.split("_")

    # Create pet_name starting as empty string
    pet_name = ""

    # Loops to check if word in pet name is only
    # alphabetic characters - if true append word
    # to pet_name separated by trailing space
    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "

    # Strip off starting/trailing whitespace characters
    pet_name = pet_name.strip()

    # Prints resulting pet_name
    print("\nFilename=", pet_image, "   Label=", pet_name)

    # Replace None with the results_dic dictionary that you created with this
    # function
    return None
