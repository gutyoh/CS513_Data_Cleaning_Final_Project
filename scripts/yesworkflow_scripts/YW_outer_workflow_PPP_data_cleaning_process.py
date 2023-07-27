# @BEGIN Outer_Workflow_PPP_Data_Cleaning_Process

    # @BEGIN OpenRefine_Cleaning
    # @IN PPP_Data_up_to_150k_080820_HI_csv @URI file:PPP_Data_up_to_150k_080820_HI.csv
    # @OUT PPP_Data_up_to_150k_080820_HI_OpenRefineCleaned_csv @URI file:PPP_Data_up_to_150k_080820_HI_OpenRefineCleaned.csv
    # @END OpenRefine_Cleaning

    # @BEGIN Python_Cleaning
    # @IN PPP_Data_up_to_150k_080820_HI_OpenRefineCleaned_csv
    # @OUT PPP_Data_up_to_150k_080820_HI_OpenRefine_PythonCleaned_csv @URI file:PPP_Data_up_to_150k_080820_HI_OpenRefine_PythonCleaned.csv
    # @END Python_Cleaning

    # @BEGIN Domain_Constraint_Checks
    # @IN PPP_Data_up_to_150k_080820_HI_OpenRefine_PythonCleaned_csv
    # @OUT PPP_Data_up_to_150k_080820_HI_OpenRefine_PythonCleaned_csv
    # @END Domain_Constraint_Checks

    # @BEGIN Python_Data_Loading_Into_SQLite_DB
    # @IN PPP_Data_up_to_150k_080820_HI_OpenRefine_PythonCleaned_csv
    # @OUT PPP_db @URI file:PPP.db
    # @END Python_Data_Loading_Into_SQLite_DB

    # @BEGIN Referential_Integrity_Checks
    # @IN PPP_db
    # @OUT PPP_db @URI file:PPP.db
    # @END Referential_Integrity_Checks

# @END Outer_Workflow_PPP_Data_Cleaning_Process
