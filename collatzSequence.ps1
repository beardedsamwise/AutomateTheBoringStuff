function collatz {
    param ($number)
    if ($number % 2 -eq 0) {
        return ($number / 2)
    }
    else {
        return (3 * $number + 1)
    }
}

$number = Read-Host -Prompt "Enter a number:"

try {
    $number = [int]$number
    while ($number -ne 1) {
        $number = collatz($number)
        Write-Host "$number"
    }
}
catch {
    Write-Host "You entered a non-integer!!!"
}


