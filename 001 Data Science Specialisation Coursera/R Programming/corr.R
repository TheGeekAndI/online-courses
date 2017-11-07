corr <- function(directory, threshold = 0) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    FilesList<-list.files(path = directory, full.names = TRUE)

    # initiate vector for correlations
    cord<-numeric(0)


    for (i in 1:332){
        # read data for the ith station
        raw<-read.csv(FilesList[i])

        # find number of complete cases
        n<-raw[complete.cases(raw),]

        #check whether complete cases are above threshold
        if(nrow(n)>threshold){
            # if they are above threshold calculate correlation of sulphate and nitrate at the station
            c<-cor(n$sulfate, n$nitrate)

            # append the correlation value to the corelations vector
            cord<-append(cord,c)
        }
    }
    return(cord)
    ## Return a numeric vector of correlations
    ## NOTE: Do not round the result!
}