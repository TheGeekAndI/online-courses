# Twitter API authentication
library(bitops)
library(RCurl)
library(RJSONIO)
library(twitteR)
library(ROAuth)
library(jsonlite)

myapp = oauth_app("twitter",key="l4N89uMVM7ql12MZdWmYew",secret="O1WBY7zK8atuyEzJEBqK0uAXzKuxlDeTx4HCuW53E8c")
sig = sign_oauth1.0(myapp,token = "317969835-Dpu41f1YMYymFPSbmKPOFcEeyvSQPWEz5MhpdKfz",token_secret = "9weJmritzNuKy5z4Ime3Fyv5yqsO0yNMNU9undgwY")
homeTL = GET("https://api.twitter.com/1.1/statuses/home_timeline.json", sig)

json1<-content(homeTL)
json2<-jsonlite::fromJSON(toJSON(json1))

con<-url('http://biostat.jhsph.edu/~jleek/contact.html')
htmlCode = readLines(con)
close(con)
c<-nchar(htmlCode)
c[c(10,20,30,100)]
