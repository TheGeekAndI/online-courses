complete <- function(directory, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    FilesList<-list.files(path = directory, full.names = TRUE)

    ## rename id vector
    stations<-id
    ## initiate empty vectors
    id<-NULL
    nobs<-NULL


    ## use a loop to append data to initialised data frame
    for(i in stations){
        # read in data
        raw<-read.csv(FilesList[i])

        # find complete cases
        n<-sum(complete.cases(raw))

        # populate vectors
        id<-append(id,i)
        nobs<-append(nobs,n)

    }

    ## Create data frame from the two vectors

    d<-data.frame(id,nobs)
    return(d)
}