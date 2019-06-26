import os
import sys
import glob

path_to_data = os.path.join("/","Users","sararey","tmp") # hard code to results directory
dirlist = os.listdir(path_to_data)

run_id = "190524_D00501_0318_BHYMM2BCX2" # need to obtain on the fly
run_id = "190607_M00766_0229_000000000-CCWJY"

run_path = os.path.join(path_to_data,run_id)

pipelines_dict = {('SomaticAmplicon', '1.7.6'): "somatic_amplicon",
                  ('GermlineEnrichment', 'num'): "germline_enrichment",
                  ('GermlineEnrichment', 'num'): "germline_enrichment_new"}

#print(run_path)
#print(glob.glob(os.path.join(p, ps, "*.variables")))

# Current versions of pipeline check?
# Load in file with currently used versions of pipeline

def main(): #pass global variables in?
    # Check results folder has been correctly created
    check_results_folder(run_path)

    # load variables file and identify pipeline- assumes that each panel has at least one sample
    try:
        print("loading variables file")
        variables_dict = load_variables(run_path)
    except:
        raise Exception("Variables file could not be loaded or parsed")

    # Identify pipeline as a list of all pipelines with versions
    pipelines = get_pipeline_name(variables_dict)
    print(pipelines)
    if len(pipelines) == 1:
        print("Only one pipeline for this run")
        print(pipelines_dict.get(pipelines[0]))




    elif len(pipelines) > 1:
        print("Logic to support multiple pipelines here- loop and call appropriate function")
    else:
        raise Exception("No pipelines in variables file")



    # Check run level processing complete if applicable- germline enrichment panels only

    # Check sample level processing complete if applicable

    return None

def somatic_amplicon():
    return "somatic"


def check_results_folder(run_directory):
    try:
        print("results folder is " + run_directory)
    except:
        raise Exception(f"There is no results folder for run {run_id} also {run_path}")

def load_variables(input_path):
    '''
    :param input_path: the path to the run folder
    :return: dictionary containing the contents of all of the variables file per sample
    '''
    # Parse all panels
    panels_fullpath = (parse_directory(input_path))
    # Create dictionary to hold all the samples as keys
    samples_dict = {}
    # Obtain samples and parse variables files
    for p in panels_fullpath:
        # Parse all samples
        samples_fullpath = parse_directory(p)
        # Iterate through all samples to load contents of variables file into a nested dictionary
        for ps in samples_fullpath:
            samples_name = os.path.split(ps)[-1]
            # Add second key to dictionary
            values_dict = {}
            # Parse variables file
            with open(os.path.join(p, samples_name, samples_name + ".variables")) as f:
                for line in f:
                    if not (line.startswith("#") or line.isspace()):
                        divide_line = line.rstrip().split("=")
                        variable = divide_line[0]
                        value = divide_line[1]
                        # Add data to dictionary
                        values_dict[variable] = value
            samples_dict[samples_name] = values_dict
    return samples_dict

def load_variables_archived(input_path):
    '''
    :param input_path: the path to the run folder
    :return: dictionary containing the contents of all of the variables file as a nested dictionary, per sample,
     per panel
    '''
    # Parse all panels
    panels_fullpath = (parse_directory(input_path))
    # Create dictionary to nest data within
    panels_dict = {}
    # Obtain samples and parse variables files
    for p in panels_fullpath:
        # Obtain just panel name without leading path
        panel_name = os.path.split(p)[-1]
        # Create dictionary to hold all the samples as keys
        samples_dict = {}
        # Parse all samples
        samples_fullpath = parse_directory(p)
        # Iterate through all samples to load contents of variables file into a nested dictionary
        for ps in samples_fullpath:
            samples_name = os.path.split(ps)[-1]
            # Add second key to dictionary
            values_dict = {}
            # Parse variables file
            with open(os.path.join(p, samples_name, samples_name + ".variables")) as f:
                for line in f:
                    if not (line.startswith("#") or line.isspace()):
                        divide_line = line.rstrip().split("=")
                        variable = divide_line[0]
                        value = divide_line[1]
                        # Add data to dictionary
                        values_dict[variable] = value
            samples_dict[samples_name] = values_dict
        panels_dict[panel_name] = samples_dict
    return panels_dict

def get_pipeline_name(dict):
    '''
    :param dict: dictionary containing the data from the variables files (output from load_variables)
    :return: list of all pipeline, version combinations present in the dataset
    '''
    pipeline_list = []
    for k in dict:
        pipeline_version= ((dict.get(k).get("pipelineName"), (dict.get(k).get("pipelineVersion"))))
        pipeline_list.append(pipeline_version)
    pipeline_set = set(pipeline_list)
    pipeline_name_samples = list(pipeline_set)
    return pipeline_name_samples


def parse_directory(input_directory):
    '''
    :param input_directory: the full path to the directory to be parsed
    :return: list of directories within the input directory
    '''
    directories_filtered = filter(lambda x: os.path.isdir(os.path.join(input_directory, x)), os.listdir(input_directory))
    directories_path_list = [os.path.join(input_directory, d) for d in directories_filtered]
    return (directories_path_list)


def check_run_level():
    return None

def check_sample_level():
    return None


if __name__ == '__main__':
        main()