<?php

$dir = '.';
$refDir = $dir.'/ref-out';

$referentialCodeFiles = getAllFiles($refDir, '!!!');
var_dump($referentialCodeFiles);
$referentialOutFiles = getAllFiles($refDir, 'out');
var_dump($referentialOutFiles);

$countOfTests = 0;
$failed = 0;

foreach ($referentialCodeFiles as $index => $refCodeFile) {

    $testFailed = false;
    ++$countOfTests;

    echo "**********************************TEST: $refCodeFile ********************************************************************".PHP_EOL;

    $actualOutput = null;
    $actualOutputFile = $dir . '/' . $referentialOutFiles[$index] . '.out';
    if(is_file($actualOutputFile)) {
        $actualOutput = trim(file_get_contents($actualOutputFile));
    }
    $actualCode = trim(file_get_contents($dir . '/' . $refCodeFile . '.!!!'));

    $expectedOutput = null;
    $expectedOutputFile = $refDir . '/' . $referentialOutFiles[$index] . '.out';
    if(is_file($expectedOutputFile)) {
        $expectedOutput = trim(file_get_contents($expectedOutputFile));
    }
    $expectedCode = trim(file_get_contents($refDir . '/' . $refCodeFile . '.!!!'));

    $diffFile = $dir . '/' . $referentialOutFiles[$index] . '.diff';
    shell_exec("touch $diffFile");

//    if ($actualOutput !== $expectedOutput) {
//        $testFailed = true;
//        echo 'FAILED'.PHP_EOL;
//
//        echo 'EXPECTED:>>>>'.PHP_EOL;
//        echo implode('', $actualOutput);
//        echo PHP_EOL.'<<<<<'.PHP_EOL;
//
//        echo 'ACTUAL:>>>>'.PHP_EOL;
//        echo $expectedOutput;
//        echo PHP_EOL.'<<<<<'.PHP_EOL;
//
//        var_dump($actualOutput, $expectedOutput);
//    } else {
//        echo 'OUTPUT OK'.PHP_EOL;
//    }

    if ($expectedCode !== $actualCode) {
        $testFailed = true;
        echo 'FAILED'.PHP_EOL;

        echo 'EXPECTED CODE:>>>>'.PHP_EOL;
        echo $expectedCode;
        echo PHP_EOL.'<<<<<'.PHP_EOL;

        echo 'ACTUAL CODE:>>>>'.PHP_EOL;
        echo $actualCode;
        echo PHP_EOL.'<<<<<'.PHP_EOL;
    } else {
        echo 'CODE OK'.PHP_EOL;
    }

    if ($testFailed) {
        ++$failed;

        echo $referentialOutFiles[$index] . ' failed with error: ' . file_get_contents($dir . '/' . $referentialOutFiles[$index] . '.err');
    }

    echo PHP_EOL.PHP_EOL;
}

$ok = $countOfTests-$failed;
echo "Passed tests: {$ok}/$countOfTests".PHP_EOL;

function getAllFiles($dir, $extension)
{
    $files = [];
    if (is_dir($dir)) {
        if ($dh = opendir($dir)) {
            while (($file = readdir($dh)) !== false) {
                if (strpos($file, '.'. $extension)) {
                    $files[] = substr($file, 0, strpos($file, '.'));
                }
            }
            closedir($dh);
        }
    }

    return $files;
}
