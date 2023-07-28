# @BEGIN Python_Data_Cleaning_Process
# @IN PPP-Data-up-to-150k-080820-HI-OpenRefineCleaned_csv @URI file:PPP-Data-up-to-150k-080820-HI-OpenRefineCleaned.csv
# @OUT PPP-Data-up-to-150k-080820-HI-OpenRefine-PythonCleaned_csv @URI file:PPP-Data-up-to-150k-080820-HI-OpenRefine-PythonCleaned.csv

    # @BEGIN LoadInitialDataset
    # @IN PPP-Data-up-to-150k-080820-HI-OpenRefineCleaned_csv
    # @OUT initial_dataframe
    # @END LoadInitialDataset

    # @BEGIN RemoveDuplicates
    # @IN initial_dataframe
    # @OUT deduplicated_dataframe
    # @END RemoveDuplicates

    # @BEGIN RectifyCityZipAssociations
    # @IN deduplicated_dataframe
    # @OUT rectified_dataframe
    # @END RectifyCityZipAssociations

    # @BEGIN LoadNAICSCodes
    # @IN industry-titles_csv @URI file:industry-titles.csv
    # @OUT naics_dataframe
    # @END LoadNAICSCodes

    # @BEGIN CleanNAICSTitles
    # @IN naics_dataframe
    # @OUT cleaned_naics_dataframe
    # @END CleanNAICSTitles

    # @BEGIN PreprocessNAICSCodes
    # @IN cleaned_naics_dataframe
    # @OUT preprocessed_naics_dataframe
    # @END PreprocessNAICSCodes

    # @BEGIN MergeDataframes
    # @IN rectified_dataframe
    # @IN preprocessed_naics_dataframe
    # @OUT merged_dataframe
    # @END MergeDataframes

    # @BEGIN ImputeMissingValue
    # @IN merged_dataframe
    # @OUT imputed_dataframe
    # @END ImputeMissingValue

    # @BEGIN ConvertNAICSCodeToString
    # @IN imputed_dataframe
    # @OUT final_dataframe
    # @END ConvertNAICSCodeToString

    # @BEGIN SaveCleanedData
    # @IN final_dataframe
    # @OUT PPP-Data-up-to-150k-080820-HI-OpenRefine-PythonCleaned_csv
    # @END SaveCleanedData

# @END Python_Data_Cleaning_Process
