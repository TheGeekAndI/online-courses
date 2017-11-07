# run analysis file which cleans and tidy's data
# load necessary packages
library(dplyr)
library(tidyr)
library(data.table)

### train file manipulation
# read train file
train<-read.table("./UCI HAR Dataset/train/X_train.txt",sep = "")

# read train labels
trainlabels<-read.table("./UCI HAR Dataset/train/y_train.txt",sep = "")
# rename the vector
trainlabels<-rename(trainlabels,label=V1)

# read subject id
subjecttrainid<-read.table("./UCI HAR Dataset/train/subject_train.txt",sep="")
# rename the vector to subject
subjecttrainid<-rename(subjecttrainid,subjectid=V1)

# combine the table wit the identifiers
traindf<-cbind(subjecttrainid,trainlabels,train)

# add a new column to label which data set (train or test) it belongs to
traindf<-mutate(traindf,set="train")

### Test file manipulation
# read test file
test<-read.table("./UCI HAR Dataset/test/X_test.txt",sep = "")

# read test labels
testlabels<-read.table("./UCI HAR Dataset/test/y_test.txt",sep = "")
# rename the vector
testlabels<-rename(testlabels,label=V1)

# read subject id
subjecttestid<-read.table("./UCI HAR Dataset/test/subject_test.txt",sep="")
# rename the vector to subject
subjecttestid<-rename(subjecttestid,subjectid=V1)

# combine the test wit the identifiers
testdf<-cbind(subjecttestid,testlabels,test)

# add a new column to label which data set (train or test) it belongs to
testdf<-mutate(testdf,set="test")

### combine the files and manipulate
# combine test and train data
df<-rbind(traindf,testdf)

# remove the test and train data sets to conserve RAM
rm(test,train,testdf,traindf)

# make df into a data table for tidyr
dt<-tbl_df(df)

# group by subjectid and label
dt<-group_by(dt,subjectid,label)

# take the mean of each variable by subject and activity
dtmean<-summarise_each(dt,funs(mean),V1:V561,set)

# extract a vector with the old variable names
oldnames<-names(dtmean)

# create vector with new names
newnames<-read.table("./UCI HAR Dataset/features.txt",sep="",stringsAsFactors =F)

# remove the row label
newnames<-newnames[,2]

# extract the vector with the old column names for the values
oldnames<-names(dtmean)

# remove the non-value column names
oldnames<-oldnames[3:563]

# set replace the old names with the new names
dtmean<-setnames(dtmean,old=oldnames,new=newnames)

# create a tidy text file
tidy<-write.table(dtmean,"./tidy.txt",row.names = F)
