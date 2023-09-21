#!/bin/ksh

#---------------------------------------------------------
# Write a script that monitors a directory for changes and 
# sends an email notification when a new file is added.
#---------------------------------------------------------

# ----- Set up variables
  watchDir="/home/$USER/Documents/WatchedDirectory/"
  emailFile="${watchDir}emailBodyText.txt"
  email="notagnuineemail@email.com"
  subject="Directory Notification"
# emailBody <- Being set below (See 'Set Email Body')


# ----- Check WatchedDireetory exist or create it
if [[ ! -e ${watchDir} ]] ;
then
  echo "Directory Not Found.... Creating: $emailFile"
  mkdir $watchDir
  touch $emailFile
  chmod 775 $emailFile
  echo "This is the email body" >> $emailFile
fi

# ----- Set Email Body
read -r emailBody < $emailFile
echo $emailBody

# ----- Set up 