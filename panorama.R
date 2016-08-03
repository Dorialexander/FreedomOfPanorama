#All the variables need to be downloaded using load("RData.Rdata")

iraMedia <- function(plot = FALSE) {
  
  #First a bit of cleaning (no variable name…) so that it looks better on the original plot
  media <- toafc[grepl("\\*media_", toafc$X), ]
  media$X <- gsub("\\*media_", "", media$X)
  media$X <- gsub("-", " ", media$X)
  dataet <- dataet[grepl("\\*media_", rownames(dataet)), ]
  rownames(dataet) <- gsub("\\*media_", "", rownames(dataet))
  rownames(dataet) <- gsub("-", " ", rownames(dataet))
  dataet$X <- rownames(dataet)

  # We use the English rather than the default French in Iramuteq
  colnames(dataet) <- gsub("classe", "Class", colnames(dataet))
  
  #We get the dominant class for each media
  dataet$classy <- colnames(dataet)[apply(dataet, 1, which.max)]
  
  #We merge both the afc coordinates and the cluster repository by "X"
  mediaall <- merge(media, dataet, by="X")

  if (plot==TRUE) {
      library(ggplot2)
      mediaplot = ggplot(mediaall, aes(x=Coord..facteur.1, y=Coord..facteur.2, label = X)) + geom_label(aes(fill = factor(classy)), color = "white") + labs(x="Dimension 1", y="Dimension 2", fill="Class")
      print(mediaplot)
    }
  
  return(mediaall)
}

iraWord <- function(numwords = 100, plot=FALSE) {
  word <- toafc[!grepl("\\*media_|\\*year_", toafc$X), ]
  wordClass <- chistabletot[!grepl("\\*media_|\\*year_", rownames(chistabletot)), ]
  wordClass <- as.data.frame(wordClass)
  
  # We use the English rather than the default French in Iramuteq
  colnames(wordClass) <- gsub("classe", "Class", colnames(wordClass))
  
  #We get the dominant class for each word
  wordClass$classy <- colnames(wordClass)[apply(wordClass, 1, which.max)]
  
  wordClass$X <- rownames(wordClass)
  
  #We merge both the afc coordinates and the cluster repository by "X"
  wordall <- merge(word[c(1:numwords),], wordClass, by="X")
  
  if (plot==TRUE) {
    
    library(ggplot2)
    wordplot <- ggplot(wordall, aes(x=Coord..facteur.1, y=Coord..facteur.2, label = X)) + geom_label(aes(fill = factor(classy)), color = "white") + labs(x="Dimension 1", y="Dimension 2", fill="Class")
    print(wordplot)
  }
  return(wordall)
}
