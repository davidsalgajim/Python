#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: David Andres Salgado Jimenez
# DATE CREATED:07/15/2022                                 
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
import os

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
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    #(1) first - lecture of image_dir path
    
    #retrieve filenames
    image_files=os.listdir(image_dir)
    
    #(2) second - creation of image label dictionary
    
    # creation of empty dictionary
    results_dic=dict()
    
    #loop to fill dictionary
    
    for image in image_files:
        
        if image.startswith("."):
            continue
        else:
        
            #lower case letters
            low_name_image=image.lower()
            
            #take out the extention if it has
            low_name_image_without_ext=os.path.splitext(low_name_image)[0]

            #split of lower case name
            word_list_image=low_name_image_without_ext.split("_")

            #image name empty
            image_name=""
        
            #check of only alphanumeric values
            for word in word_list_image:
                if word.isalpha():
                    image_name+=word+" "
         
            #strip to eliminate whitespaces characters
            image_name=image_name.strip()

            #print resulting name
            print ("\n filename=",image,"  label=",image_name)

            #add key-value pairs inside dictionary
            if image not in results_dic:
                results_dic[image]=[image_name]
            else:
                print("**warning key= ",image,
                      " already exist in results_dic with value =",
                      results_dic[image])         
    
    return results_dic
