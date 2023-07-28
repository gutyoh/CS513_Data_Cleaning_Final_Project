# @BEGIN Load_Data_Into_SQLite_DB_Process
# @IN PPP-Data-up-to-150k-080820-HI-OpenRefine-PythonCleaned_csv @URI file:PPP-Data-up-to-150k-080820-HI-OpenRefine-PythonCleaned.csv
# @OUT PPP_db @URI file:PPP.db

    # @BEGIN LoadCleanedDataset
    # @IN PPP-Data-up-to-150k-080820-HI-OpenRefine-PythonCleaned_csv
    # @OUT cleaned_dataframe
    # @END LoadCleanedDataset

    # @BEGIN CreateSQLiteDB
    # @OUT PPP_db
    # @END CreateSQLiteDB

    # @BEGIN CreateTableAddresses
    # @IN PPP_db
    # @OUT Addresses_table
    # @END CreateTableAddresses

    # @BEGIN CreateTableDemographics
    # @IN PPP_db
    # @OUT Demographics_table
    # @END CreateTableDemographics

    # @BEGIN CreateTableBusinessTypes
    # @IN PPP_db
    # @OUT BusinessTypes_table
    # @END CreateTableBusinessTypes

    # @BEGIN CreateTableIndustries
    # @IN PPP_db
    # @OUT Industries_table
    # @END CreateTableIndustries

    # @BEGIN CreateTableLoans
    # @IN PPP_db
    # @OUT Loans_table
    # @END CreateTableLoans

    # @BEGIN CreateAddressesDataFrame
    # @IN cleaned_dataframe
    # @OUT addresses_dataframe
    # @END CreateAddressesDataFrame

    # @BEGIN CreateDemographicsDataFrame
    # @IN cleaned_dataframe
    # @OUT demographics_dataframe
    # @END CreateDemographicsDataFrame

    # @BEGIN CreateBusinessTypesDataFrame
    # @IN cleaned_dataframe
    # @OUT businessTypes_dataframe
    # @END CreateBusinessTypesDataFrame

    # @BEGIN CreateIndustriesDataFrame
    # @IN cleaned_dataframe
    # @OUT industries_dataframe
    # @END CreateIndustriesDataFrame

    # @BEGIN InsertIntoAddressesTable
    # @IN addresses_dataframe
    # @IN Addresses_table
    # @OUT populated_Addresses_table
    # @END InsertIntoAddressesTable

    # @BEGIN InsertIntoDemographicsTable
    # @IN demographics_dataframe
    # @IN Demographics_table
    # @OUT populated_Demographics_table
    # @END InsertIntoDemographicsTable

    # @BEGIN InsertIntoBusinessTypesTable
    # @IN businessTypes_dataframe
    # @IN BusinessTypes_table
    # @OUT populated_BusinessTypes_table
    # @END InsertIntoBusinessTypesTable

    # @BEGIN InsertIntoIndustriesTable
    # @IN industries_dataframe
    # @IN Industries_table
    # @OUT populated_Industries_table
    # @END InsertIntoIndustriesTable

    # @BEGIN InsertIntoLoansTable
    # @IN cleaned_dataframe
    # @IN populated_Addresses_table
    # @IN populated_Demographics_table
    # @IN populated_BusinessTypes_table
    # @IN populated_Industries_table
    # @IN Loans_table
    # @OUT populated_Loans_table
    # @END InsertIntoLoansTable

# @END Load_Data_Into_SQLite_DB_Process
