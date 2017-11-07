# This function calculates the mean of a pollutant (sulfate or nitrate) across a specified list
# of monitors.The function 'pollutantmean' takes three arguments: 'directory', 'pollutant',
# and 'id'. Given a vector monitor ID numbers, 'pollutantmean' reads that monitors' particulate
# matter data from the directory specified in the 'directory' argument and returns the mean of
# the pollutant across all of the monitors, ignoring any missing values coded as NA.

pollutantmean <- function(directory, pollutant, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    FilesList<-list.files(path = directory, full.names = TRUE)

    ## 'pollutant' is a character vector of length 1 indicating
    ## the name of the pollutant for which we will calculate the
    ## mean; either "sulfate" or "nitrate".


    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used

    # initialise an empty data frame
    selData<-data.frame()

    # use a loop to append data to initialised data frame
    for(i in id){
        selData<-rbind(selData,read.csv(FilesList[i]))
    }

    ## Return the mean of the pollutant across all monitors list
    ## in the 'id' vector (ignoring NA values)
    ## NOTE: Do not round the result!

    # find the mean depending on the pollutant
    if(pollutant=="sulfate"){
        round(mean(selData$sulfate,na.rm = T),3)
    } else if(pollutant=='nitrate'){
        round(mean(selData$nitrate,na.rm = T),3)
    }
}
