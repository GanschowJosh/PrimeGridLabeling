source=../CoprimeLinker/*.c
binary=../CoprimeLinker/test
testsZip=../Data/testCases.7z
tests=./testCases
passed=1

gcc $source -o $binary

7z x $testsZip > /dev/null

for n in {1..50}; 
do
    $binary $n 0
    if [ "$(md5sum $tests/linkedCoprimes-"$n".txt | awk '{print $1}')" == "$(md5sum ../Data/linkedCoprimes.txt | awk '{print $1}')" ];
        then echo "Passed case for max = $n" 
    else 
        echo "Failed case '$n'"
        $passed=0
    fi
done


rm -rf $tests

rm $binary

if [ $passed == 1 ];
    then echo "All cases passed!"
else
    echo "One or more cases failed!"
fi