<?php

$point = 289326;
$index = 1;
$x = 0;
$y = 0;
$steps = 1;
$left = false;
$right = true;
$up = false;
$down = false;
$direction = 0;
$matrix[0][0] = 1;
while ($index <= $point) {
    $forFuckSake = 0;
    while ($forFuckSake < 2) {
        $step = 1;
        while ($step <= $steps) {
            if ($left) $x++;
            elseif ($right) $x--;
            elseif ($up) $y++;
            elseif ($down) $y--;

            $matrix[$x][$y] = calcValue($matrix, $x, $y);

            if ($matrix[$x][$y] > $point) {
                echo $matrix[$x][$y];
                return;
            }

            $index++;
            $step++;
        }
        if ($direction < 3) {
            $direction++;
        } else {
            $direction = 0;
        }
        switch ($direction) {
            case 0: // right
                $right = true; $left = false; $up = false; $down = false;
                break;
            case 1: // up
                $up = true; $left = false; $right = false; $down = false;
                break;
            case 2: // left
                $left = true; $right = false; $up = false; $down = false;
                break;
            case 3: // down
                $down = true; $left = false; $up = false; $right = false;
                break;
        }
        $forFuckSake++;
    }
    $steps++;
}

function calcValue($matrix, $x, $y)
{
    $value = 0;
    if (isset($matrix[$x+1][$y])) {
        $value += $matrix[$x+1][$y];
    }
    if (isset($matrix[$x+1][$y+1])) {
        $value += $matrix[$x+1][$y+1];
    }
    if (isset($matrix[$x][$y+1])) {
        $value += $matrix[$x][$y+1];
    }
    if (isset($matrix[$x-1][$y+1])) {
        $value += $matrix[$x-1][$y+1];
    }
    if (isset($matrix[$x-1][$y])) {
        $value += $matrix[$x-1][$y];
    }
    if (isset($matrix[$x-1][$y-1])) {
        $value += $matrix[$x-1][$y-1];
    }
    if (isset($matrix[$x][$y-1])) {
        $value += $matrix[$x][$y-1];
    }
    if (isset($matrix[$x+1][$y-1])) {
        $value += $matrix[$x+1][$y-1];
    }
    return $value;
}