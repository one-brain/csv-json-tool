import csv, json, os
from os import listdir
from os.path import isfile, join


# Function to convert csv to json
# csvFilePath: path of csv file
# jsonFilePath: path of json file
def make_json(csvFilePath, jsonFilePath):
    #create a dictionary

    if(csvFilePath.endswith('csv')==False):
        print('not a csv file', csvFilePath)
        return
    
    data=[]

    try:
        # open a csv reader called DictReader
        with open(csvFilePath, encoding='unicode_escape') as csvf:
            csvReader = csv.DictReader(csvf)

            #convert eachrow into a dictionary
            #and add it to data
            for rows in csvReader:
                #Assuming a column named 'No' to 
                #to b the primary key
                #key = rows['edgegatewayid']
                data.append(rows)
                #print(data)

            # Open a json writer, and use the json.dumps()  
            # function to dump data
            with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data,indent=4))
            
            print('Generated '+ jsonFilePath + ' for ' + csvFilePath)
    except Exception as e:
        print('failed to make json file ', csvFilePath)
        


# Function to convert all csv files in given source directory
# sourceDir: path to the directory where csv files exist
# outputDir: path to the directory where json files will be created
def convert_all_csv_files_to_json(sourceDir,outputDir):
    try:
        delete_all_files(outputDir,'.json')
        print('\n')
        onlyfiles = [f for f in listdir(sourceDir) if isfile(join(sourceDir, f))]
        for fileName in onlyfiles:
            csvFilePath = os.path.join(sourceDir,fileName)
            jsonFilePath = os.path.join(outputDir,fileName.replace('.csv','.json'))
            # Call the make_json function
            make_json(csvFilePath, jsonFilePath)
    except Exception as e:
        print('Failed to convert all csv files to json, Reason ',e )



# Function to delete all files in directory.
# directoryPath: path of the directory for cleanup
# extension: file extension
def delete_all_files(directoryPath, extension):
    try:    
        #print('Deleting all ' + extension + ' files in directory '+ directoryPath)
        filelist = [ f for f in os.listdir(directoryPath) if f.endswith(extension) ]
        for f in filelist:
            print('DELETED : '+os.path.join(directoryPath,f))
            os.remove(os.path.join(directoryPath, f))
    except Exception as ex:
        print('Failed to delete all files, Reason '+ex)






inputDir = r'.\input'
outputDir = r'.\output'

# Call the convert_all_csv_files_to_json function
convert_all_csv_files_to_json(inputDir,outputDir)