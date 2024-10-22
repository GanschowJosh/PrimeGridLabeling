source=../CoprimeLinker/*.c
binary=../CoprimeLinker/test

gcc $source -o $binary

for n in {1..50}; 
do
    $binary $n 0
    if [ "$(md5sum ../Data/testCases/linkedCoprimes-"$n".txt | awk '{print $1}')" == "$(md5sum ../Data/linkedCoprimes.txt | awk '{print $1}')" ];
        then echo "Passed case '$n'" 
    else 
        echo "Failed case '$n'"
    fi
done

rm $binary