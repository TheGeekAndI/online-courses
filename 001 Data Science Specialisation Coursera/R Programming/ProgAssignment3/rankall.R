rankall <- function(outcome, num = "best") {
    ## Read outcome data
    outcomeData<-read.csv("outcome-of-care-measures.csv", colClasses = "character")

    ## Check that state and outcome are valid
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

    # only keep the data for the specified outcome
    outcomeData<-outcomeData[,c(2,7,colID)]
    outcomeData[,3]<-as.numeric(outcomeData[,3])

    # Keep only complete cases
    outcomeData<-outcomeData[complete.cases(outcomeData),]

    ## For each state, find the hospital of the given rank
    # split the data into a list by state, apply the ranking and combine the list back
    # into a data frame

    # split data into a list
    splitData<-split(outcomeData,outcomeData$State)

    # define the ranking function
    # function takes a block (list of data by state) and rank to be returned
    r<-function(stateData,num){
        # order the state data
        ordState<-order(stateData[,2],stateData[,3],stateData[,1],na.last = NA)

        if(num=="best"){
            stateData$Hospital.Name[ordState[1]]
        }else if(num=="worst"){
            stateData$Hospital.Name[ordState[length(ordState)]]
        }else if(is.numeric(num)){
            stateData$Hospital.Name[ordState[num]]
        }else{
            stateData$Hospital.Name[ordState[NA]]
        }
    }

    # use lapply to apply function
    hospitalByState<-lapply(splitData,r,num)

    # return in a data frame
    data.frame(hospital=unlist(hospitalByState),state=names(hospitalByState))

}