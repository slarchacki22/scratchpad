#!/bin/bash

##########################################################
##########################################################
# updates old *.m3u8 key reference from
# #EXT-X-KEY:METHOD=AES-128,URI="https://yourdomain.com:8443/key?kid=1&productionId=<contentid>”
# to current key reference
# #EXT-X-KEY:METHOD=AES-128,URI="https://yourdomain.com:8443/[subdirectory]/key?id=<contentid>”
# and creates backup .bak of old file if a change is made
#########################################################
#########################################################


# use -force option to recover *.m3u8 file from *.bak

if [[ $1 == "-force" ]]
then 
    for dir in [insert_directory] 
    do
        for file in $(find $dir -name "*bak" -follow)
        do
            mv $file ${file/.bak/}
            echo "Reverting back from *.bak to new *.m3u8"
        done      
    done
    sync
else
    for dir in [insert_directory]
    do
        count=$(find $dir -name "*.bak" -follow | wc -l)
        if [ $count == 0 ]
        then
            find $dir -name "*.m3u8*" -follow -exec sed -i.bak 's!key?kid=1&productionId![subdirectory]/key?id!' {} \;
            echo "Modifying *.m3u8 file in $dir"       
        #else
        #    echo "Skipping...already changed key for $dir"
        fi
        count=$(find $dir -name "*.bak2" -follow | wc -l)
        if [ $count == 0 ]
        then
            find $dir -name "*.m3u8" -follow -exec sed -i.bak2 's!domain.com:8443!domain.com!' {} \;
            echo "Removing port 8443 from key line, $dir/*.m3u8"
        fi
    done
   sync
fi
