gcc ../CoprimeLinker/*.c -o ../CoprimeLinker/test

for n in {1..50}; 
do
    ../CoprimeLinker/test $n
    if [ "$(md5sum ../Data/testCases/linkedCoprimes-"$n".txt | awk '{print $1}')" == "$(md5sum ../Data/linkedCoprimes.txt | awk '{print $1}')" ];
        then echo "Passed case '$n'" 
    else 
        echo "Failed case '$n'"
    fi
done

rm ../CoprimeLinker/test