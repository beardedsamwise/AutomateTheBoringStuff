# This program lets the user type in an integer that then 
# keeps calling collatz() on that number until the function returns the value 1
# For more info: https://en.wikipedia.org/wiki/Collatz_conjecture

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


