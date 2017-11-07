rankhospital <- function(state, outcome, num = "best") {
    ## Read outcome data
    outcomeData<-read.csv("outcome-of-care-measures.csv", colClasses = "character")

    # extract list of state values
    # create unique list of state values
    stateList<-unique(outcomeData[,7])
    outcomeList<-c('heart attack','heart failure','pneumonia')

    # check if "state" is in the list
    if(state %in% stateList){
        # only keep the data in the state
        stateData<-outcomeData[which(outcomeData$State==state),]
    } else {
        stop("invalid state")
    }

    # check if the "outcome" is valid in nested if statement
    if(outcome %in% outcomeList){
        # set a variable to select the relevant outcome data
        # HA = 11, HF = 17, P = 23
        if(outcome=='heart attack'){
            colID<-11
        }else if(outcome=='heart failure'){
            colID<-17
        }else if(outcome=='pneumonia'){
            colID<-23
        }else{
            stop('invalid outcome')
        }
    } else {
        stop("invalid outcome")
    }

    # only take the hospital name (column 2) & outcome columns
    rankData<-stateData[,c(2,colID)]
    rankData[,2]<-as.numeric(rankData[,2])

    # order from lowest rate to highest rate
    # if 2 have the same rate order alphabetically
    orderedData<-rankData[order(rankData[,2],rankData[,1]),]

    # if a hospital doesnt have data exclude it
    orderedData<-orderedData[complete.cases(orderedData),]

    # make specified ranka a numeric variable
    if(num=="best"){
        hospitalName<-orderedData[1,1]
    }else if(num=="worst"){
        hospitalName<-orderedData[nrow(orderedData),1]
    }else if(num>nrow(orderedData)){
        hospitalName<-NA
    }else{
        hospitalName<-orderedData[num,1]
    }

    ## Return hospital name in that state with the given rank
    return(hospitalName)

}