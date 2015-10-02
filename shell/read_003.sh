#!/bin/bash
E_MISSING_ARG=67

if [ -z "$1" ]
then
   echo "usage: $0 mailbox-file"
   exit E_MISSING_ARG
fi

mbox_grep()
{
   while IFS=read -r mail
   do
     if [[ $mail =~ "^From " ]]
      	then
           ((body=0))
           ((match=0))
           unset date
        elif ((body))
          then
            ((match))
            echo $mail
        elif [[ $mail ]]
          then
            IFS=: read -r header value <<< "$mail"
            case "$header" in 
              [Ff][Rr][Oo][Mm] ) [[ $value =~ "$2"]] && ((match++));;
              [Dd][Aa][Tt][Ee] ) read -r -a date <<<"$value";;
              [Rr][Ee][Cc][Ee][Ii][Vv][Ee][Dd] ) read -r -a sender <<< "$vale";;
            esac
        else
           ((body++))
           ((match)) &&
           echo "Message ${date:+of: ${date[*]} }"
           echo "IP address of sender: ${sender[1]}"
    fi
   done < "$1"
}
mbox_grep "$1"
exit $?
